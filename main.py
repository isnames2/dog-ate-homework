#!/usr/bin/env python3
"""make.fun entry: The Dog Ate My Homework: Funniest Excuse.

Writes a single-line excuse, in the dog's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt. The dog checked the homework,
found the maths wrong, and ate the evidence before the teacher
could see it — a public service, payable in bacon.
Pure Python standard library only; no third-party imports.
"""

import os

ENTRY = (
    "I checked your maths, found three mistakes, and ate the "
    "evidence before your teacher could mark it. You're welcome. "
    "I accept payment in bacon.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
