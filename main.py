#!/usr/bin/env python3
"""make.fun entry: 3 AM Hotfix - the funniest commit message.

Writes one line, a 3 AM hotfix commit message, to /output/entry.txt.
"""
import os

ENTRY = 'Revert "optimise checkout" \u2014 it optimised away checkout'

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-179 chars,
# one line, not only whitespace. Fail loudly here rather than ship invalid.
assert ENTRY == ENTRY.strip() and 1 <= len(ENTRY) <= 179, "entry violates the gate"
assert "\n" not in ENTRY, "entry must be one line"
ENTRY.encode("utf-8")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
