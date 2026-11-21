#!/usr/bin/env python3
"""Write a one-line joke about working beside an AI coding agent.

The program writes the joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(or ``/output/entry.txt`` when the variable is unset) as UTF-8 text.
Standard library only; no network access.
"""

import os
import sys
from pathlib import Path

# The joke itself: one line, 153 characters, about an AI pair
# programmer taking over during a live demo.
JOKE_PARTS = (
    "During the live demo, my AI pair programmer rewrote the feature ",
    "in a language I don't speak, on a branch I can't find \u2014 while ",
    "I nodded like I planned it.",
)

# Gate from the competition rules: entry.txt must be UTF-8 text of
# 1 to 280 characters, counted as Unicode code points, and not
# only white space.
MIN_CHARS = 1
MAX_CHARS = 280
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def build_joke() -> str:
    """Assemble the one-line joke from its parts."""
    return "".join(JOKE_PARTS)


def validate(text: str) -> str:
    """Return the stripped joke, or fail if it breaks the gate."""
    cleaned = text.strip()
    if not cleaned:
        raise SystemExit("joke must not be only white space")
    if not MIN_CHARS <= len(cleaned) <= MAX_CHARS:
        raise SystemExit("joke must be 1-280 characters")
    return cleaned


def output_dir() -> Path:
    """Resolve where entry.txt goes from the environment."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def write_entry(text: str, directory: Path) -> Path:
    """Write the joke as UTF-8 text and return the file path."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / OUTPUT_FILENAME
    target.write_text(text, encoding="utf-8")
    return target


def main(argv: list[str] | None = None) -> int:
    """Build, validate and write the joke; 0 on success."""
    del argv  # No command-line arguments are used.
    joke = validate(build_joke())
    write_entry(joke, output_dir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
