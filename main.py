"""make.fun bounty entry: The Meeting That Should Have Been an Email.

Writes the single entry line (one joke, at most 200 characters) to
entry.txt inside MAKEFUN_OUTPUT_DIR (fallback /output). Deterministic,
byte-identical across runs, no trailing newline. Python stdlib only.
"""

import os
import sys

ENTRY = (
    "This meeting could have been an email, but then nobody would have "
    "spent an hour nodding at a slide they could have ignored in four "
    "seconds."
)

MAX_CHARS = 200


def gate(line):
    """Refuse any line that would fail the bounty gate."""
    if not line:
        raise SystemExit("gate: entry is blank")
    if len(line) > MAX_CHARS:
        raise SystemExit("gate: entry exceeds %d chars" % MAX_CHARS)
    if "\n" in line or "\r" in line:
        raise SystemExit("gate: entry must be a single line")
    if line != line.strip():
        raise SystemExit("gate: entry has leading/trailing whitespace")
    return line


def main():
    line = gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read back and confirm the file holds exactly the gated line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise SystemExit("verify: entry.txt does not match the gated line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
