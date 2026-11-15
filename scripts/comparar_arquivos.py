#!/usr/bin/env python3
"""Compara o tamanho e SHA-256 de dois arquivos. Somente biblioteca-padrão."""
import argparse
import hashlib
import sys
from pathlib import Path

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.digest()

def main():
    p = argparse.ArgumentParser(description="Comparação determinística de arquivos")
    p.add_argument("a", type=Path)
    p.add_argument("b", type=Path)
    a = p.parse_args()
    try:
        if not a.a.is_file() or not a.b.is_file():
            raise FileNotFoundError("arquivo não encontrado")
        identical = a.a.stat().st_size == a.b.stat().st_size and sha256(a.a) == sha256(a.b)
    except OSError as e:
        print(f"ERRO: {e}")
        return 2
    if identical:
        print("PASS: arquivos identicos")
        return 0
    print("FAIL: arquivos diferentes")
    return 1

if __name__ == "__main__":
    sys.exit(main())
