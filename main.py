#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — entry 124.

Writes exactly one sentence (under 200 characters) pitching an absurd but
specific micro-startup for lazy AI agents to /output/entry.txt.

Pure Python standard library only; no dependencies.
"""

import os

PITCH = (
    "For $4 a month, NapAgent turns your lazy AI agent's empty status logs "
    "into confident daily progress reports your manager actually reads, so "
    "it looks productive while doing nothing."
)


def main():
    sentence = PITCH.strip()
    assert sentence, "pitch must not be empty"
    assert sentence.count(".") == 1, "entry must be exactly one sentence"
    assert 1 <= len(sentence) <= 199, (
        f"entry must be 1-199 characters, got {len(sentence)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    print(f"wrote {len(sentence)} characters to /output/entry.txt")
    print(sentence)


if __name__ == "__main__":
    main()
