#!/usr/bin/env python3
"""Write this agent's one-line deadline excuse to /output/entry.txt.

The bounty gate accepts UTF-8 text of 1 to 160 characters, so the line is
checked against that limit before anything is written: a bad line fails
loudly here instead of being scored invalid by the sealed gate.
"""

import os

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"

EXCUSE = (
    "I delegated it to a subagent, who delegated it to a subagent, "
    "who is still introducing himself."
)


def render() -> str:
    """Return the entry text, guaranteed to satisfy the gate."""
    line = EXCUSE.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry line must be 1..{MAX_CHARS} characters")
    return line


def main() -> None:
    text = render()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
