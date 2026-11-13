import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
S = ROOT / 'workflows/fluxo_com_checkpoints.py'
spec = importlib.util.spec_from_file_location('checkpoint_workflow', S)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class StateTest(unittest.TestCase):
    def fixture(self, dir):
        root = dir / 'book'
        (root/'chapters').mkdir(parents=True)
        (root/'scripts').mkdir()
        (root/'_quarto.yml').write_text('project: test\n', encoding='utf-8')
        (root/'index.qmd').write_text('# Apresentação\n', encoding='utf-8')
        (root/'chapters/a.qmd').write_text('# Teste\n', encoding='utf-8')
        for name in ['verificar_boxes.py','verificar_estrutura.py']:
            (root/'scripts'/name).write_text('import sys\nsys.exit(0)\n', encoding='utf-8')
        return root

    def test_normal_and_idempotent_resume(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);root=self.fixture(d);work=d/'runs'
            self.assertEqual(mod.run(root,work), 0)
            first=json.loads((work/'state.json').read_text())
            self.assertEqual(first['state'],'WAITING_HUMAN')
            self.assertEqual(first['approval_status'],'NOT_GRANTED')
            self.assertEqual(mod.run(root,work), 0)
            self.assertEqual(first,json.loads((work/'state.json').read_text()))

    def test_injected_failure_and_resume(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);root=self.fixture(d);work=d/'runs'
            self.assertEqual(mod.run(root,work,'after-inventory'),4)
            before=json.loads((work/'state.json').read_text())
            self.assertEqual(before['state'],'INTERRUPTED')
            self.assertEqual(mod.run(root,work),0)
            after=json.loads((work/'state.json').read_text())
            self.assertEqual(after['state'],'WAITING_HUMAN')
            self.assertGreater(len(after['events']),len(before['events']))

    def test_source_changed_blocks_old_checkpoint(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);root=self.fixture(d);work=d/'runs'
            self.assertEqual(mod.run(root,work,'after-inventory'),4)
            (root/'chapters/a.qmd').write_text('# Alterado\n',encoding='utf-8')
            self.assertEqual(mod.run(root,work),3)
            self.assertEqual(json.loads((work/'state.json').read_text())['state'],'BLOCKED')

    def test_structure_failure_does_not_approve(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);root=self.fixture(d);work=d/'runs'
            (root/'scripts/verificar_boxes.py').write_text('import sys\nsys.exit(1)\n',encoding='utf-8')
            self.assertEqual(mod.run(root,work),2)
            state=json.loads((work/'state.json').read_text())
            self.assertEqual(state['state'],'STRUCTURE_FAILED')
            self.assertEqual(state['approval_status'],'NOT_GRANTED')

    def test_state_must_be_outside_root(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td);root=self.fixture(d)
            with self.assertRaises(ValueError): mod.run(root,root/'dist')


if __name__=='__main__': unittest.main()
