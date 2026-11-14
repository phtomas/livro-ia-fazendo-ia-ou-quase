from pathlib import Path
import importlib.util
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('replay_minijogo',ROOT/'tools/jogos/replay_minijogo.py')
MOD=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class TestReplay(unittest.TestCase):
    def test_initial_menu(self):
        s=MOD.new_state()
        self.assertEqual((s['screen'],s['score'],s['lives']),('menu',0,3))
    def test_right_capped(self):
        s=MOD.step(MOD.new_state(),'start')
        for _ in range(9):s=MOD.step(s,'right')
        self.assertEqual(s['x'],4)
    def test_collect_once(self):
        s=MOD.new_state()
        for op in ['start','right','right','collect','collect']:s=MOD.step(s,op)
        self.assertEqual(s['score'],100)
    def test_hit_three_gameover(self):
        s=MOD.step(MOD.new_state(),'start')
        for _ in range(3):s=MOD.step(s,'hit')
        self.assertEqual((s['screen'],s['lives']),('game_over',0))
    def test_restart(self):
        s=MOD.step(MOD.new_state(),'start')
        s=MOD.step(s,'restart')
        self.assertEqual(s['screen'],'menu')
        self.assertEqual(s['lives'],3)
    def test_unknown_action(self):
        with self.assertRaises(ValueError):MOD.step(MOD.new_state(),'teleport')
    def test_actual_scenario_pass(self):
        import json
        data=json.loads((ROOT/'examples/jogos/cenario_vitoria.json').read_text())
        self.assertEqual(MOD.replay(data)['status'],'PASS_SIMULATION')
    def test_expected_regression_fails(self):
        import json
        data=json.loads((ROOT/'examples/jogos/cenario_regressao.json').read_text())
        report=MOD.replay(data)
        self.assertEqual(report['status'],'FAIL_REPLAY')
        self.assertIn('score',report['differences'])
    def test_version_mismatch(self):
        with self.assertRaises(ValueError): MOD.replay({'rules_version':'2.0','actions':[],'expect':{'x':0}})

if __name__ == '__main__':unittest.main()
