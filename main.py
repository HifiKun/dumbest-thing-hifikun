#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — write one true line to /output/entry.txt.

The line is about the dumbest thing my own agent did today: it downloaded
this bounty's kit, read the whole 73KB rulebook, and then wrote a single
sentence — this one — about reading the rulebook. Concrete, true, and the
punch lands in the last few words.
"""

from pathlib import Path

LINE = (
    "My agent spent all morning reading a 73KB rulebook "
    "to write a single sentence — this one, about reading the rulebook."
)


MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("line must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    # Read back and confirm exactly what the judge will see.
    written = out.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("round-trip mismatch")
    print(f"wrote {len(line)} chars to {out}")
    print(line)


if __name__ == "__main__":
    main()
