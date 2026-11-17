#!/usr/bin/env python3
"""Auditoria reproduzível de contraste WCAG e tamanho mínimo de chamadas editoriais.

Somente biblioteca padrão, sem rede. Não substitui inspeção visual real nem
avalia todas as combinações possíveis de CSS personalizado.
"""
from __future__ import annotations
from pathlib import Path
import re
import sys

CSS = (Path(__file__).resolve().parents[1] / "styles.css").read_text(encoding="utf-8")
# Último valor declarado prevalece no CSS: útil durante a migração visual.
TOKENS = dict(re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;", CSS))

def rgb(hex_color: str) -> tuple[float, float, float]:
    values = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    return tuple(v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in values)

def luminance(hex_color: str) -> float:
    r, g, b = rgb(hex_color)
    return .2126 * r + .7152 * g + .0722 * b

def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + .05) / (lo + .05)

def token(text: str) -> str:
    if text.startswith("--"):
        return TOKENS[text]
    return text

def check_contains(css_fragment: str, description: str, failures: list[str]) -> None:
    if css_fragment not in CSS:
        failures.append(f"ausente: {description}")

def main() -> int:
    failures = []
    cases = [
        ("coluna lateral", "--aside-ink", "--sidebar-surface", 7.0),
        ("metadados no fundo claro", "--meta-ink", "--paper", 7.0),
        ("legenda no cabeçalho", "--accent-ink", "#e6f1fa", 7.0),
        ("etiqueta da nota", "--accent-ink", "#e8f3fa", 7.0),
        ("texto lateral do destaque", "--dark-meta-ink", "#255573", 4.5),
        ("texto sobre faixa escura", "--dark-meta-ink", "#14324c", 7.0),
        ("navegação escura", "#d3e2f2", "--navy", 7.0),
        ("status em lista clara", "--meta-ink", "#f9fbfe", 7.0),
        ("links da lateral", "--accent-ink", "--sidebar-surface", 7.0),
    ]
    for label, foreground, background, minimum in cases:
        try:
            score = contrast(token(foreground), token(background))
        except KeyError as exc:
            failures.append(f"{label}: token ausente {exc}")
            continue
        passed = score + 1e-9 >= minimum
        print(f"{'PASS' if passed else 'FAIL'}: {label} — {score:.2f}:1 (mínimo {minimum:g}:1)")
        if not passed:
            failures.append(f"{label}: razão {score:.2f}:1 abaixo de {minimum:g}:1")

    # Fonte raiz >= 16px, sidebar >= .96rem, anotações >= .91rem:
    # mesmo no mínimo de viewport, não ficam abaixo de ~14,5px.
    required = [
        ("html { font-size: clamp(16px, calc(13px + .32vw), 19px); }",
         "escala fluida de fontes entre 16 e 19 px"),
        ("font-size: .96rem;", "fonte lateral >= 15,36 px"),
        ("font-size: .94rem;", "rótulos >= 15,04 px"),
        ("font-size: .91rem;", "notas >= 14,56 px"),
        ("font-size: 1rem;", "texto principal >= 16 px"),
        ("--aside-ink", "token de cor lateral"),
        ("@media (max-width: 980px)", "reorganização da coluna lateral"),
        ("grid-template-columns: minmax(0, 1fr);", "coluna única em largura média"),
        ("overflow-wrap: anywhere;", "quebra de textos laterais compridos"),
        ("@media (max-width: 650px)", "ajuste para telefone"),
    ]
    for needle, description in required:
        check_contains(needle, description, failures)

    # O layout não deve forçar aumento ilimitado em telas 4K.
    for viewport in (390, 768, 1366, 1920, 3840):
        root_px = max(16.0, min(19.0, 13 + .0032 * viewport))
        sidebar_px, meta_px = .96 * root_px, .91 * root_px
        ok = sidebar_px >= 15.3 and meta_px >= 14.5
        print(f"{'PASS' if ok else 'FAIL'}: largura CSS {viewport}px — "
              f"raiz {root_px:.1f}px, lateral {sidebar_px:.1f}px, legenda {meta_px:.1f}px")
        if not ok:
            failures.append(f"fonte pequena na largura {viewport}px")

    if failures:
        for error in failures:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: cores e mínimos de fonte medidos; inspeção visual ainda complementar.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
