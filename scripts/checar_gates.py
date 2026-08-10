#!/usr/bin/env python3
"""Verifica se os artefatos obrigatórios de uma peça existem.

Uso:
    python3 scripts/checar_gates.py <slug-da-peca> [--pipeline camada3_execucao]

O agente roda isto antes de mostrar qualquer peça ao humano. Enquanto houver
artefato faltando ou vazio, a peça não é entregável.

Existe porque checkpoint declarado sem arquivo já entregou peça reprovada.
Ver marca/memory/casos-de-falha.md.
"""

import argparse
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
MIN_LINHAS = 5


def carregar_squad():
    return yaml.safe_load((RAIZ / "squad.yaml").read_text(encoding="utf-8"))["squad"]


def carregar_pipeline(squad, nome: str):
    if nome not in squad:
        disponiveis = [k for k in squad if k.startswith(("camada", "pipeline"))]
        raise SystemExit(f"pipeline '{nome}' não existe. disponíveis: {disponiveis}")
    return squad[nome]


def secoes_faltando(caminho: Path, especificacao: dict) -> list:
    """Seções que a especificação do artefato exige e o arquivo não tem."""
    if not especificacao:
        return []
    texto = caminho.read_text(encoding="utf-8")
    return [s for s in especificacao.get("secoes_obrigatorias", []) if s not in texto]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("peca", help="slug da peça, o mesmo usado em marca/output/")
    parser.add_argument("--pipeline", default="camada3_execucao")
    args = parser.parse_args()

    squad = carregar_squad()
    passos = carregar_pipeline(squad, args.pipeline)
    especificacoes = squad.get("artefatos", {})
    faltando, vazios, incompletos, ok = [], [], [], []

    for passo in passos:
        modelo = passo.get("artefato")
        if not modelo:
            continue
        caminho = RAIZ / modelo.format(peca=args.peca)
        rotulo = f"{passo['passo']} -> {caminho.relative_to(RAIZ)}"
        if not caminho.exists():
            faltando.append(rotulo)
            continue
        if len(caminho.read_text(encoding="utf-8").strip().splitlines()) < MIN_LINHAS:
            vazios.append(rotulo)
            continue
        ausentes = secoes_faltando(caminho, especificacoes.get(caminho.stem))
        if ausentes:
            incompletos.append(f"{rotulo}  (sem: {', '.join(ausentes)})")
        else:
            ok.append(rotulo)

    for item in ok:
        print(f"  ok          {item}")
    for item in incompletos:
        print(f"  INCOMPLETO  {item}")
    for item in vazios:
        print(f"  VAZIO       {item}")
    for item in faltando:
        print(f"  FALTANDO    {item}")

    problemas = len(faltando) + len(vazios) + len(incompletos)
    if problemas:
        print(
            f"\nPeça '{args.peca}' NÃO é entregável: {len(faltando)} faltando, "
            f"{len(vazios)} vazio(s), {len(incompletos)} incompleto(s)."
        )
        print("Produza os artefatos antes de mostrar a peça ao humano.")
        return 1

    print(f"\nPeça '{args.peca}': todos os artefatos de gate presentes e completos.")
    print("Lembrete: desvio de gramática não declarado e não autorizado bloqueia a entrega.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
