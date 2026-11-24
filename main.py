#!/usr/bin/env python3
"""Houseplant Out-of-Office -- make.fun entry (program/v1).

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (or $ENTRY_OUT when set).

The line: the fern has had enough. Its human left for the holidays
and forgot to water it back in March, so the fern files its own
out-of-office reply -- and forwards everything to the cactus.
"""

import os
import sys

# The entry: one line, at most 120 characters, plant voice throughout.
ENTRY = (
    "Out of office \u2014 so am I. The fern resigned in March: "
    "no water, no sun, no respect. Email the cactus."
)

MAX_CHARS = 120


def main() -> int:
    """Write ENTRY to the output file and sanity-check the gate."""
    out = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars (limit {MAX_CHARS})",
              file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
