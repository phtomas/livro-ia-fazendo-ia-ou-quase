#!/usr/bin/env python3
"""Regressão de navegação do portal: abas obrigatórias e destinos existentes.

Somente biblioteca padrão. Não faz chamadas externas nem altera páginas.
Os 21 arquivos q/*.html são redirecionamentos dos QR Codes, não páginas.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ["Início", "Capítulos", "Laboratório", "Complementos", "Atualizações"]
DESTINATIONS = {
    "Início": "index.html",
    "Capítulos": "SUMARIO.html",
    "Laboratório": "laboratorio/README.html",
    "Complementos": "complementos/index.html",
    "Atualizações": "ATUALIZACOES_E_ERRATAS.html",
}

class NavigationParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_nav = False
        self.depth = 0
        self.current = None
        self.links = []
        self.nav_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav" and attrs.get("aria-label") == "Navegação principal":
            self.nav_count += 1
            self.in_nav = True
            self.depth = 1
            return
        if not self.in_nav:
            return
        if tag == "nav":
            self.depth += 1
        if tag == "a":
            self.current = {
                "href": attrs.get("href", ""),
                "active": attrs.get("aria-current") == "page",
                "text": "",
            }

    def handle_data(self, data):
        if self.current is not None and self.in_nav:
            self.current["text"] += data

    def handle_endtag(self, tag):
        if not self.in_nav:
            return
        if tag == "a" and self.current is not None:
            self.current["text"] = " ".join(self.current["text"].split())
            self.links.append(self.current)
            self.current = None
        if tag == "nav":
            self.depth -= 1
            if self.depth == 0:
                self.in_nav = False

def expected_active(path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    if relative == "index.html":
        return "Início"
    if relative == "SUMARIO.html":
        return "Capítulos"
    if relative == "ATUALIZACOES_E_ERRATAS.html":
        return "Atualizações"
    if relative.startswith("complementos/"):
        return "Complementos"
    return "Laboratório"

def pages():
    result = [ROOT / "index.html", ROOT / "SUMARIO.html",
              ROOT / "ATUALIZACOES_E_ERRATAS.html"]
    for directory in ("laboratorio", "docs", "complementos"):
        result.extend((ROOT / directory).rglob("*.html"))
    return sorted(result)

def validate(path: Path) -> list[str]:
    relative = path.relative_to(ROOT).as_posix()
    errors = []
    parser = NavigationParser()
    parser.feed(path.read_text(encoding="utf-8"))
    if parser.nav_count != 1:
        return [f"{relative}: esperado 1 menu principal, encontrado {parser.nav_count}"]
    labels = [link["text"] for link in parser.links]
    if labels != EXPECTED:
        errors.append(f"{relative}: abas {labels!r}, esperadas {EXPECTED!r}")
    active = [link["text"] for link in parser.links if link["active"]]
    if active != [expected_active(path)]:
        errors.append(f"{relative}: aba ativa {active!r}, esperada {[expected_active(path)]!r}")
    for link in parser.links:
        url = link["href"]
        split = urlsplit(url)
        if split.scheme or split.netloc or not split.path:
            errors.append(f"{relative}: menu externo ou vazio: {url!r}")
            continue
        target = (path.parent / split.path).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            errors.append(f"{relative}: destino inexistente: {url!r}")
        elif link["text"] in DESTINATIONS and target != (ROOT / DESTINATIONS[link["text"]]).resolve():
            errors.append(f"{relative}: destino errado para {link['text']}: {url!r}")
    return errors

def main() -> int:
    paths = pages()
    errors = [item for path in paths for item in validate(path)]
    for error in errors:
        print("FAIL:", error)
    if errors:
        print(f"FAIL: {len(errors)} falhas em {len(paths)} páginas")
        return 1
    print(f"PASS: {len(paths)} páginas, cinco abas estáveis, destinos internos corretos e estado ativo único.")
    print("NOTA: valida estrutura dos arquivos HTML; testes visuais e navegação no navegador são distintos.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
