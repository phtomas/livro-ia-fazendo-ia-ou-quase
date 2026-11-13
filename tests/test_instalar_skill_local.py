"""Testes locais de empacotamento; NÃO testam modelos/hosts de skills."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/"tools/skills/instalar_skill_local.py"
spec=importlib.util.spec_from_file_location("instalar_skill_local",SCRIPT)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class InstallSkillTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.src=self.root/"skill"
        (self.src/"references").mkdir(parents=True)
        (self.src/"SKILL.md").write_text("---\nname: revisao-autoral\ndescription: >-\n  Revise textos técnicos. Usar para revisão autoral.\n---\n# Instruções\n",encoding="utf-8")
        (self.src/"references"/"contrato.md").write_text("Não alterar fatos.\n",encoding="utf-8")
        self.ws=self.root/"workspace"
        self.ws.mkdir()

    def cli(self,*args):
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            code=mod.run(["--source",str(self.src),"--workspace",str(self.ws),"--json",*args])
        self.assertEqual(code,0)
        return json.loads(stdout.getvalue())

    def test_dry_run_is_read_only(self):
        data=self.cli()
        self.assertEqual(data["mode"],"DRY_RUN")
        self.assertFalse((self.ws/".agents").exists())
        self.assertFalse((self.ws/".claude").exists())
        self.assertTrue(all(x["status"]=="READY" for x in data["results"]))

    def test_apply_two_targets_and_integrity(self):
        data=self.cli("--apply")
        self.assertTrue(all(x["status"]=="INSTALLED" for x in data["results"]))
        orig=mod.inventory(self.src)
        for folder in (".agents/skills", ".claude/skills"):
            self.assertEqual(mod.inventory(self.ws/folder/"revisao-autoral"),orig)

    def test_idempotence(self):
        self.cli("--apply")
        data=self.cli("--apply")
        self.assertTrue(all(x["status"]=="ALREADY_CURRENT" for x in data["results"]))
        self.assertFalse(any(x["written"] for x in data["results"]))

    def test_conflict_fails_before_mutation(self):
        self.cli("--apply")
        changed=self.ws/".agents/skills/revisao-autoral/SKILL.md"
        changed.write_text("usuário mudou localmente",encoding="utf-8")
        with self.assertRaises(mod.SkillError):
            self.cli("--apply")
        self.assertEqual(changed.read_text(encoding="utf-8"),"usuário mudou localmente")

    def test_replace_creates_backup(self):
        self.cli("--apply")
        changed=self.ws/".agents/skills/revisao-autoral/SKILL.md"
        changed.write_text("mudança local",encoding="utf-8")
        data=self.cli("--apply","--replace")
        self.assertEqual(data["results"][0]["status"],"REPLACED")
        backup=Path(data["results"][0]["backup"])
        self.assertEqual((backup/"SKILL.md").read_text(encoding="utf-8"),"mudança local")
        self.assertEqual(mod.inventory(self.ws/".agents/skills/revisao-autoral"),mod.inventory(self.src))

    def test_invalid_metadata_fails(self):
        (self.src/"SKILL.md").write_text("# Sem frontmatter\n",encoding="utf-8")
        with self.assertRaises(mod.SkillError):
            self.cli()

    def test_missing_required_entry_fails(self):
        (self.src/"SKILL.md").unlink()
        with self.assertRaises(mod.SkillError):
            self.cli()

    def test_symlinks_rejected(self):
        (self.src/"references"/"external").symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(mod.SkillError):
            self.cli()

if __name__=="__main__": unittest.main()
