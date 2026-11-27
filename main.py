#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry for u-puan-describe-your-ex-in-one-word-9fc6ebe7.

Writes the single-word verdict to /output/entry.txt.
"""
import os

ENTRY = "Unsubscribe"

# The gate requires exactly one word, 1-111 chars, nothing else attached.
assert ENTRY and len(ENTRY) <= 111 and not any(c.isspace() for c in ENTRY)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
