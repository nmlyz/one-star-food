#!/usr/bin/env python3
"""Write one sentence to /output/entry.txt.

The sentence is a one-star review of Earth from an alien tourist who
still admits the food was excellent: the locals breed peppers purely
to hurt themselves, then brag about surviving the burn, but the mapo
tofu underneath the pain was the best thing the tourist ate on this
planet. The program keeps the sentence as one constant, checks it
against the entry gate, writes it, and reads the file back to confirm
the bytes it wrote.
"""

import os
import sys

LINE = (
    "One star: the locals breed peppers purely to hurt themselves, "
    "then brag about surviving the burn, but the mapo tofu underneath "
    "the pain was the best thing I ate on this planet."
)


def check(line):
    if not 1 <= len(line) <= 200:
        return f"line is {len(line)} characters, gate needs 1-200"
    if line.count(".") != 1 or not line.endswith("."):
        return "line must be exactly one sentence"
    if "\n" in line or line != line.strip():
        return "line must be a single line with no surrounding space"
    return None


def main():
    error = check(LINE)
    if error:
        sys.exit(error)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("written bytes do not match")
    print(f"wrote {len(data)} bytes ({len(LINE)} chars) to {path}")


if __name__ == "__main__":
    main()
