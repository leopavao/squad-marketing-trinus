#!/usr/bin/env python3
"""Verifica as invariantes do squad. Roda no CI a cada push.

Existe porque regra escrita em markdown some sem ninguém perceber. Em
2026-08-10 uma regra foi sobrescrita por outro agente e a peça seguinte
foi reprovada pelo cliente. Ver marca/memory/casos-de-falha.md.

    python3 scripts/checar_invariantes.py
"""

import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent

# Arquivos que precisam falar da regra das três camadas.
PONTOS_DE_ENTRADA = [
    "README.md",
    "squad.yaml",
    "marca/memory/memoria-criativa.md",
    "marca/design-system/gramatica-carrossel.md",
    "core/agents/designer/brief.md",
    "core/agents/diretor-criativo/brief.md",
]

OBRIGATORIOS = [
    "squad.yaml",
    "marca/design-system/gramatica-carrossel.md",
    "marca/design-system/base-carrossel/base.css",
    "marca/memory/casos-de-falha.md",
    "marca/referencias/README.md",
]

REVOGADAS = ["CREDITO-BARATO-CUSTO-LIDO-DIREITO", "CINCO-PERGUNTAS-ANTES-DE-COMPRAR"]

falhas = []


def erro(msg):
    falhas.append(msg)


def checar_arquivos_obrigatorios():
    for rel in OBRIGATORIOS:
        if not (RAIZ / rel).exists():
            erro(f"arquivo obrigatório sumiu: {rel}")


def checar_yaml():
    try:
        squad = yaml.safe_load((RAIZ / "squad.yaml").read_text(encoding="utf-8"))["squad"]
    except Exception as exc:
        erro(f"squad.yaml não parseia: {exc}")
        return
    passos = squad.get("camada3_execucao", [])
    com_artefato = [p for p in passos if p.get("artefato")]
    if len(com_artefato) < 4:
        erro(
            "camada3_execucao perdeu gates com artefato "
            f"(esperado 4 ou mais, encontrado {len(com_artefato)})"
        )


def checar_regra_presente():
    for rel in PONTOS_DE_ENTRADA:
        caminho = RAIZ / rel
        if not caminho.exists():
            erro(f"ponto de entrada sumiu: {rel}")
            continue
        if "três camadas" not in caminho.read_text(encoding="utf-8").lower():
            erro(f"a regra das três camadas sumiu de {rel}")


def checar_revogadas():
    """As revogadas só podem aparecer nas notas que registram a revogação."""
    permitidos = {"marca/memory/memoria-criativa.md", "marca/memory/indice-criativos.md"}
    for caminho in RAIZ.rglob("*.md"):
        if ".git" in caminho.parts:
            continue
        rel = caminho.relative_to(RAIZ).as_posix()
        if rel in permitidos:
            continue
        texto = caminho.read_text(encoding="utf-8", errors="ignore")
        for nome in REVOGADAS:
            if nome in texto:
                erro(f"referência revogada citada em {rel}: {nome}")


def checar_referencias():
    base = RAIZ / "marca/referencias"
    if not base.exists():
        return
    for html in sorted(base.glob("*/index.html")):
        rel = html.relative_to(RAIZ).as_posix()
        texto = html.read_text(encoding="utf-8")

        if "base-carrossel/base.css" not in texto:
            erro(f"{rel} não linka a base do design system")

        if not (html.parent / "ficha.md").exists():
            erro(f"{rel} está sem ficha.md")

        # Hex escrito dentro das telas: a peça tem que usar os tokens.
        deck = texto.partition('<section class="deck">')[2].rpartition("</section>")[0]
        hexes = set(re.findall(r"#[0-9a-fA-F]{6}\b", deck))
        if hexes:
            erro(f"{rel} declara cor fora dos tokens: {', '.join(sorted(hexes))}")

        # Locação única: todas as telas apontam para o mesmo arquivo.
        fotos = set(re.findall(r'class="photo"[^>]*src="([^"]+)"', texto))
        if len(fotos) > 1:
            erro(f"{rel} usa {len(fotos)} locações diferentes: {', '.join(sorted(fotos))}")


def main() -> int:
    checar_arquivos_obrigatorios()
    checar_yaml()
    checar_regra_presente()
    checar_revogadas()
    checar_referencias()

    if falhas:
        print(f"{len(falhas)} invariante(s) quebrada(s):\n")
        for f in falhas:
            print(f"  x  {f}")
        print("\nAlguma regra estrutural do squad foi removida ou contrariada.")
        print("Se a mudança for intencional, atualize também scripts/checar_invariantes.py.")
        return 1

    print("Invariantes do squad: tudo no lugar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
