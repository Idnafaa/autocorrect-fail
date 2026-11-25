#!/usr/bin/env python3
"""Funniest Autocorrect Fail — one-line fail writer.

Writes a single original autocorrect-fail line (1-199 chars) to
/output/entry.txt. The line is one text message gone wrong: the phone
swapped one small word, and the reply makes the damage obvious.
"""
import os

FAIL = (
    "I texted my fiancée 'I can't wait to marry you' and autocorrect "
    "sent 'I can't wait to bury you' — she replied 'the wedding is off.'"
)


def main():
    text = FAIL.strip()
    if not (1 <= len(text) <= 199):
        raise ValueError(f"entry is {len(text)} chars, must be 1-199")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
