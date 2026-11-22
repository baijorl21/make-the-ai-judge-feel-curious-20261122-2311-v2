#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun entry.

Writes one short text (1-280 Unicode code points) meant to intrigue
its reader and leave them wanting more, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt in the sandbox). Stdlib only, no
network, deterministic.
"""

import os
import sys

# The text: a clockmaker's daughter who hears a second ticking beneath
# the tower's. The intrigue is in what is not explained — a slower,
# patient time kept for someone who has not arrived yet — and the
# image stays after the last line.
TEXT = (
    "The clockmaker's daughter could diagnose any clock by ear: a worn "
    "gear, a tired spring, a chime that lied. One morning she pressed "
    "her ear to the tower and heard, beneath its ticking, a second "
    "ticking — slower, patient, keeping time for someone who had not "
    "arrived yet."
)

MAX_CODE_POINTS = 280


def check(text):
    """Hold the text to the gate's caps before it is written out."""
    text = text.strip()
    if not text:
        raise ValueError("text is only white space")
    if len(text) > MAX_CODE_POINTS:
        raise ValueError(f"text is {len(text)} code points, over {MAX_CODE_POINTS}")
    return text


def main():
    text = check(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
