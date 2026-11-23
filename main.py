#!/usr/bin/env python3
"""Write grandma's one word about AI to /output/entry.txt.

Entry for make.fun's "One Word From Grandma": the single word a
grandma would text about AI. The word chosen hears "ChatGPT" the
way a grandma would — as something involving tea — so the mishearing
and the hospitality land in the same word.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "ChatGPtea"
TEXT = LINE + "\n"

MIN_CHARS = 1
MAX_CHARS = 30


def validate(text: str) -> None:
    """Reject anything the gate or the one-word form would reject."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if len(body.split()) != 1 or " " in body:
        raise ValueError("entry must be exactly one word, no spaces")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    validate(TEXT)
    payload = TEXT.encode("utf-8")
    target = out_dir / "entry.txt"
    target.write_bytes(payload)
    if target.read_bytes() != payload:
        raise IOError("read-back mismatch on entry.txt")


if __name__ == "__main__":
    main()
