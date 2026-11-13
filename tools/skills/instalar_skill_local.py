#!/usr/bin/env python3
"""Copia uma Agent Skill canônica para destinos locais, com simulação por padrão.

Sem rede, sem IA, sem instalação global. Requer Python 3.10+.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
import uuid
from pathlib import Path

HERE = Path(__file__).resolve()
DEFAULT_SOURCE = HERE.parents[2] / "skills" / "revisao-autoral"
TARGETS = {"agents": ".agents/skills", "claude": ".claude/skills"}


class SkillError(Exception):
    pass


def read_metadata(file: Path) -> tuple[str, str]:
    text = file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SkillError("SKILL.md sem frontmatter YAML inicial")
    pieces = text.split("\n---\n", 1)
    if len(pieces) < 2:
        raise SkillError("SKILL.md sem fechamento do frontmatter")
    head = pieces[0][4:]
    found = re.search(r"(?m)^name:[ \t]*(.+?)[ \t]*$", head)
    if not found:
        raise SkillError("frontmatter sem name")
    name = found.group(1).strip().strip("'\"")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise SkillError("name inválido (usar letras minúsculas, números e hífens)")
    descr = re.search(r"(?m)^description:[ \t]*(.*)$", head)
    if not descr:
        raise SkillError("frontmatter sem description")
    first = descr.group(1).strip()
    if first in (">", ">-", "|", "|-") or not first:
        after = head[descr.end():].lstrip("\n").splitlines()
        lines = []
        for line in after:
            if line.startswith(("  ", "\t")):
                lines.append(line.strip())
            elif not line.strip() and lines:
                continue
            else:
                break
        description = " ".join(lines).strip()
    else:
        description = first.strip("'\"")
    if not description or len(description) > 1024:
        raise SkillError("description ausente ou longa demais")
    return name, description


def inventory(directory: Path) -> dict[str, str]:
    if not directory.is_dir() or directory.is_symlink():
        raise SkillError(f"origem/destino não é diretório válido: {directory}")
    result: dict[str, str] = {}
    for f in directory.rglob("*"):
        if f.is_symlink():
            raise SkillError(f"link simbólico não permitido no pacote: {f}")
        if f.is_file():
            result[f.relative_to(directory).as_posix()] = hashlib.sha256(f.read_bytes()).hexdigest()
    return result


def prepare(source: Path, workspace: Path, selected: list[str]):
    if not workspace.is_dir():
        raise SkillError("workspace inexistente: crie a pasta antes de usar")
    if source.resolve() == workspace.resolve():
        raise SkillError("a origem da skill não deve ser o próprio workspace")
    source_index = inventory(source)
    if "SKILL.md" not in source_index:
        raise SkillError("origem sem SKILL.md")
    name, description = read_metadata(source / "SKILL.md")
    plans = []
    for target in selected:
        dst_base = workspace / TARGETS[target]
        dst = dst_base / name
        if dst.is_symlink() or dst_base.is_symlink():
            raise SkillError("link simbólico em destino não permitido")
        if dst.exists():
            dst_index = inventory(dst)
            status = "ALREADY_CURRENT" if dst_index == source_index else "CONFLICT"
        else:
            status = "READY"
        plans.append((target, dst, status))
    return name, description, source_index, plans


def run(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="pasta canônica da skill")
    ap.add_argument("--workspace", type=Path, required=True, help="raiz do projeto de destino")
    ap.add_argument("--targets", choices=["agents", "claude", "both"], default="both")
    ap.add_argument("--apply", action="store_true", help="efetua instalação local; padrão é somente simular")
    ap.add_argument("--replace", action="store_true", help="com --apply, guarda backup e substitui cópia divergente")
    ap.add_argument("--json", action="store_true", help="imprime relatório JSON")
    args = ap.parse_args(argv)
    selected = list(TARGETS) if args.targets == "both" else [args.targets]
    if args.replace and not args.apply:
        raise SkillError("--replace só vale com --apply")
    name, description, index, plans = prepare(args.source, args.workspace, selected)
    if args.apply and not args.replace and any(status == "CONFLICT" for _, _, status in plans):
        raise SkillError("cópia divergente encontrada; nenhuma alteração efetuada. Use --replace com cautela")
    results=[]
    for target, dst, status in plans:
        record={"target":target,"destination":str(dst),"status":status,"written":False,"backup":None}
        if args.apply and status != "ALREADY_CURRENT":
            dst.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix=".skill-stage-", dir=dst.parent) as stage_dir:
                staging=Path(stage_dir)/name
                shutil.copytree(args.source, staging, symlinks=False)
                if inventory(staging) != index:
                    raise SkillError("integridade da cópia temporária falhou")
                backup=None
                if status=="CONFLICT":
                    backup=dst.with_name(dst.name+".backup-"+uuid.uuid4().hex[:12])
                    dst.rename(backup)
                    record["backup"]=str(backup)
                try:
                    staging.rename(dst)
                    if inventory(dst) != index:
                        raise SkillError("integridade do destino falhou")
                except Exception:
                    if dst.exists():
                        shutil.rmtree(dst)
                    if backup:
                        backup.rename(dst)
                    raise
                record.update(status="REPLACED" if backup else "INSTALLED",written=True)
        results.append(record)
    output={"skill":name,"description":description,"source":str(args.source),"files":len(index),"mode":"APPLY" if args.apply else "DRY_RUN","results":results,"behavior_tested":False}
    print(json.dumps(output,ensure_ascii=False,indent=2) if args.json else "\n".join(f"{r['target']}: {r['status']} → {r['destination']}" for r in results))
    return 0


if __name__=="__main__":
    try:
        sys.exit(run())
    except (SkillError, OSError, UnicodeError) as err:
        print(f"NO-GO: {err}",file=sys.stderr)
        sys.exit(2)
