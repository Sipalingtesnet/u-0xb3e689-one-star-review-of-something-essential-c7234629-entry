#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes exactly one deadpan one-star review to /output/entry.txt, or to the
directory named by MAKEFUN_OUTPUT_DIR (the kit's dev override).

Standard library only. No network, no clock, no randomness, no input: the
review is a single constant, so every run writes the same bytes.

The text is validated against the competition's gate before it is written, so a
bad edit fails loudly here instead of quietly costing the entry.
"""

import os
import sys

# The entry: one line, deadpan, one star, the sting in the last few words.
REVIEW = (
    "One star. Sleep takes a third of my life in nightly instalments "
    "and has never once shown me the work."
)

# The gate: UTF-8 text, 1 to 160 characters, not only white space, single line.
MAX_CHARS = 160


def validate(text):
    """Fail loudly on anything the competition's gate would refuse."""
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        raise SystemExit(
            "review is %d characters; the gate allows 1 to %d" % (chars, MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("review is only white space; the gate refuses it")
    if "\n" in text or "\r" in text:
        raise SystemExit("review spans more than one line; the entry is a single line")


def output_dir():
    """The grader's /output, or the dev override when it is set and non-empty."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    validate(REVIEW)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    # newline="" so no platform newline translation can touch the exact bytes.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
