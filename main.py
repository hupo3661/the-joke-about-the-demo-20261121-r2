#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

The joke is written to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or
``/output/entry.txt`` when the variable is unset), as UTF-8 text.
Standard library only; no network access.
"""

import os
from pathlib import Path

JOKE = (
    "During the live demo, my AI pair programmer rewrote the feature "
    "in a language I don't speak, on a branch I can't find \u2014 while "
    "I nodded like I planned it."
)


def main() -> None:
    text = JOKE.strip()
    if not text or not (1 <= len(text) <= 280):
        raise SystemExit("joke must be 1-280 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
