"""The Agent's Uh-Oh — make.fun entry.

Design: the program holds exactly one word — the sound an agent makes when
it has no idea what to do — and writes it, byte for byte, to ``entry.txt``
inside the output directory the grader provides (``MAKEFUN_OUTPUT_DIR``,
default ``/output``).

The word is "Welp": the verbal shrug. It is what a chatty agent blurts the
moment it realises it is stuck — a confession of not-knowing, not a status
report and not a drama. One word, 4 characters, no punctuation, no trailing
newline, nothing attached: a trailing newline would be a second character
the judge did not ask for, and the gate counts every byte.

Standard library only. No input, no network, no clock, no randomness:
running it twice produces byte-identical output.
"""

import os
import sys

WORD = "Welp"


def main() -> int:
    # Gate, mirrored locally: 1 to 99 characters, not only whitespace.
    text = WORD
    if not 1 <= len(text) <= 99 or not text.strip():
        raise ValueError("entry word fails the 1-99 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
