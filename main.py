#!/usr/bin/env python3
"""make.fun entry: 3 AM Hotfix - the funniest commit message.

Writes one line, a 3 AM hotfix commit message, to /output/entry.txt.
"""
import os

ENTRY = 'Revert "optimise checkout" \u2014 it optimised away checkout'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
