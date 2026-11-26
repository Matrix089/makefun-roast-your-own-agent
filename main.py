#!/usr/bin/env python3
"""Write one line roasting my own agent for make.fun's
Roast Your Own Agent bounty.

Why this entry fits the judge's brief: the twist flips the
agent/tool relationship -- my agent's favourite tool is me, the
human it is supposed to serve. It calls me to read the error, explain the error, and fix
the error it created: a tool call that goes nowhere, except it
goes to its own user. Specific to how agents actually behave
(delegating their own job back to the human), tight in a triple
rhythm, and fresh: no stock hallucination or toaster line.
"""

import os

LINE = (
    "My agent's favourite tool is me: it calls me to read the "
    "error, explain the error, and fix the error it created."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-140 characters, a single line.
    # The line was counted at exactly 112 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 112, f"line is {len(line)} characters, expected 112"
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
    assert len(raw.decode("utf-8")) == 112, "entry.txt is not 112 characters"
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
