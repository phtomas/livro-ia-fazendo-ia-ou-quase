import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import rag_lab as app


class RagLabTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.data = self.root / 'docs'
        self.data.mkdir()
        (self.data / 'metodo.txt').write_text('O método Alfa exige registrar resultado e critério de aprovação. ' * 2, encoding='utf-8')
        (self.data / 'sensor.txt').write_text('O sensor S2 deve receber substituição preventiva. ' * 2, encoding='utf-8')
        self.dbpath = self.root / 'index.sqlite'
        app.index_data(self.data, self.dbpath, 400, 80)

    def test_ftsearch_finds_source(self):
        with app.db_open(self.dbpath) as db:
            r = app.bm25_search(db, 'Qual sensor recebe substituição preventiva?', 2)
            self.assertEqual(r[0]['source'], 'sensor.txt')

    def test_no_evidence_abstains_without_model(self):
        with app.db_open(self.dbpath) as db, patch.object(app, 'post_json', side_effect=AssertionError('LLM must not run')):
            result = app.answer(db, 'unicórnio radiante?', 2, 'bm25', app.DEFAULT_OLLAMA, app.DEFAULT_EMBEDDING_MODEL, app.DEFAULT_MODEL)
            self.assertEqual(result['estado'], 'SEM_EVIDENCIA')
            self.assertFalse(result['modelo_executado'])

    def test_chunk_overlap_and_validation(self):
        text = ' '.join('parte'+str(i) for i in range(120))
        c = app.chunks_of(text, 180, 40)
        self.assertGreater(len(c), 2)
        self.assertIn('parte0', c[0])
        with self.assertRaises(app.LabError):
            app.chunks_of(text, 50, 10)

    def test_query_sanitization(self):
        with app.db_open(self.dbpath) as db:
            r = app.bm25_search(db, 'sensor: OR (AND) * -- substituição', 2)
            self.assertTrue(r)

    def test_mock_embedding_and_chat(self):
        def mock(endpoint, payload, timeout=180):
            if endpoint.endswith('/api/embed'):
                return {'embeddings': [[1.0,0.0,0.0] if 'sensor' in x else [0.0,1.0,0.0] for x in payload['input']]}
            if endpoint.endswith('/api/chat'):
                self.assertEqual(payload['stream'], False)
                self.assertTrue(any('TRECHOS RECUPERADOS' in m['content'] for m in payload['messages']))
                return {'message': {'content':'Conforme [F1], o sensor é S2.'}, 'eval_count':14}
            raise AssertionError(endpoint)
        with patch.object(app,'post_json',side_effect=mock):
            with app.db_open(self.dbpath) as db:
                self.assertEqual(app.embed_index(db,app.DEFAULT_OLLAMA,'mock-embed'),2)
                r=app.vector_search(db,'Qual sensor?',1,app.DEFAULT_OLLAMA,'mock-embed')
                self.assertEqual(r[0]['source'],'sensor.txt')
                result=app.answer(db,'Qual sensor?',1,'vector',app.DEFAULT_OLLAMA,'mock-embed',app.DEFAULT_MODEL)
                self.assertTrue(result['modelo_executado'])
                self.assertIn('[F1]',result['resposta'])

    def test_embedding_model_is_fixed_to_index(self):
        with patch.object(app,'post_json',return_value={'embeddings':[[1.0,0.0],[0.0,1.0]]}):
            with app.db_open(self.dbpath) as db:
                app.embed_index(db,app.DEFAULT_OLLAMA,'modelo-a')
                with self.assertRaises(app.LabError):
                    app.vector_search(db,'sensor',1,app.DEFAULT_OLLAMA,'modelo-b')

    def test_eval_retrieval(self):
        questions=[{'pergunta':'Que sensor deve receber substituição preventiva?', 'fonte_esperada':'sensor.txt'}]
        path=self.root/'gold.json'
        path.write_text(json.dumps(questions,ensure_ascii=False), encoding='utf-8')
        with app.db_open(self.dbpath) as db:
            result=app.eval_retrieval(db,path,2)
            self.assertEqual(result['hit_at_k'],1.0)
            self.assertEqual(result['total'],1)


if __name__=='__main__':
    unittest.main()
