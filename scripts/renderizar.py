#!/usr/bin/env python3
"""Renderiza uma referência ou peça em PNG, para o agente conseguir ver.

    python3 scripts/renderizar.py marca/referencias/2026-08-10-comprar-a-vista

Gera uma prancha de conferência ao lado do index.html. Serve para comparar
a peça nova com a referência sem depender de acesso ao Drive.
"""

import subprocess
import sys
from pathlib import Path

CHROMES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
]


def achar_chrome() -> str:
    for c in CHROMES:
        if Path(c).exists():
            return c
        if "/" not in c and subprocess.run(["which", c], capture_output=True).returncode == 0:
            return c
    raise SystemExit("Chrome ou Chromium não encontrado. Instale um dos dois para renderizar.")


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    pasta = Path(sys.argv[1]).resolve()
    html = pasta / "index.html" if pasta.is_dir() else pasta
    if not html.exists():
        raise SystemExit(f"não encontrei {html}")

    saida = html.parent / "prancha.png"
    subprocess.run(
        [
            achar_chrome(), "--headless", "--disable-gpu", "--hide-scrollbars",
            f"--screenshot={saida}", "--window-size=1260,1700", f"file://{html}",
        ],
        check=True,
        capture_output=True,
    )
    print(f"prancha: {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
