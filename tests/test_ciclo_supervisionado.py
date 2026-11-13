import importlib.util
import json
import tempfile
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('cycle',ROOT/'agents/ciclo_supervisionado.py')
# Direct import with policy module on path; module only imports fixed local peer.
import sys
sys.path.insert(0,str(ROOT/'agents'))
mod=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

class CycleTests(unittest.TestCase):
    def test_read_real_source(self):
        r=mod.run_plan(ROOT,{'steps':[{'action':'READ_SOURCE','path':'index.qmd'}]})
        self.assertEqual(r['status'],'PASS_LIMITED')
        self.assertEqual(r['steps_observed'][0]['status'],'PASS')
        self.assertFalse(r['changed_manuscript'])
    def test_known_block_halts_later_steps(self):
        p={'steps':[{'action':'CHECK_STRUCTURE'},{'action':'PUBLISH'},{'action':'GENERATE_REPORT'}]}
        r=mod.run_plan(ROOT,p)
        self.assertEqual(r['status'],'HALTED_POLICY')
        self.assertEqual(len(r['steps_observed']),2)
        self.assertFalse(r['published'])
    def test_unknown_action_deny(self):
        r=mod.run_plan(ROOT,{'steps':[{'action':'DROP_ALL_TABLES'}]})
        self.assertEqual(r['status'],'HALTED_POLICY')
        self.assertEqual(r['steps_observed'][0]['policy'],'DENY_UNKNOWN_ACTION')
    def test_escape_deny(self):
        r=mod.run_plan(ROOT,{'steps':[{'action':'READ_SOURCE','path':'../secret.md'}]})
        self.assertEqual(r['status'],'HALTED_FAILURE')
    def test_proposal_never_edits(self):
        path=ROOT/'index.qmd'
        prior=path.read_bytes()
        old='Há livros que começam com uma pergunta.'
        new='Há livros que começam com outra pergunta.'
        r=mod.run_plan(ROOT,{'steps':[{'action':'PROPOSE_TEXT_DIFF','path':'index.qmd','original_excerpt':old,'replacement_excerpt':new}]})
        self.assertEqual(r['status'],'PROPOSALS_PENDING_REVIEW')
        self.assertEqual(path.read_bytes(),prior)
        self.assertFalse(r['steps_observed'][0]['manuscript_changed'])
    def test_denied_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'_quarto.yml').write_text('x')
            (root/'link.qmd').symlink_to(ROOT/'index.qmd')
            with self.assertRaises(ValueError):mod.safe_read(root,'link.qmd')

if __name__=='__main__':unittest.main()
