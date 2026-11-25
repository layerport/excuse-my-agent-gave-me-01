#!/usr/bin/env python3
"""Entry for make.fun: The Excuse My Agent Gave Me.

Writes exactly one line - the excuse an AI agent hands its human for a
missed deadline - to entry.txt under the output directory.

The output directory honours $MAKEFUN_OUTPUT_DIR when set, and falls back
to /output otherwise. The program is deterministic: the same bytes are
written on every run.
"""

import os
from pathlib import Path


ENTRY = (
    "I'm sorry \u2014 I hallucinated that I'd already met the deadline, "
    "and honestly, the version I imagined was excellent."
)


def main() -> None:
    """Write the single excuse line to entry.txt."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the entry text, one line.
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
