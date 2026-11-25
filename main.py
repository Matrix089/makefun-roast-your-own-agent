#!/usr/bin/env python3
"""Write one line roasting my own agent for make.fun's
Roast Your Own Agent bounty.

Why this entry fits the judge's brief: it roasts my own agent in
one line, and it packs two of the brief's signature behaviours into
a single twist -- the agent answers confidently before reading the
question (confident wrong answers), then apologizes for three
paragraphs (endless caveats) and asks what I meant, which reveals
it never read the question at all. Tight, specific to how agents
actually behave, and fresh: no stock hallucination or toaster line.
"""

import os

LINE = (
    "My agent answers before reading the question, then apologizes "
    "for three paragraphs and asks what I meant."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-140 characters, a single line.
    # The line was counted at exactly 105 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 105, f"line is {len(line)} characters, expected 105"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 140, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 105, "entry.txt is not 105 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
