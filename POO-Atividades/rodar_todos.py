"""Roda todos os scripts das pastas numeradas e mostra OK / FALHOU.

Uso:  python rodar_todos.py
Serve para conferir, antes de entregar/commitar, que nada quebrou.
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
ENTRADAS = {"caixa_eletronico.py": "1\n100\n3\n4\n"}  # entrada simulada do menu


def main() -> int:
    falhas = 0
    scripts = sorted(
        p for p in RAIZ.rglob("*.py") if p.resolve() != Path(__file__).resolve()
    )
    for script in scripts:
        resultado = subprocess.run(
            [sys.executable, script.name],
            cwd=script.parent,
            input=ENTRADAS.get(script.name, ""),
            capture_output=True,
            text=True,
            timeout=30,
        )
        ok = resultado.returncode == 0
        print(("OK     " if ok else "FALHOU ") + str(script.relative_to(RAIZ)))
        if not ok:
            falhas += 1
            print(resultado.stderr)
    print(f"\n{len(scripts) - falhas}/{len(scripts)} scripts executaram sem erro.")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
