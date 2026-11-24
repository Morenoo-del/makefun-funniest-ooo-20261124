#!/usr/bin/env python3
"""Write one line of an out-of-office auto-reply to /output/entry.txt.

The entry is a single line of text, 140 characters or fewer, and nothing
else: no image, no link, no second line.
"""

import os

ENTRY = (
    "I am out of the office until Monday. My inbox is being handled by my "
    "cat, who has already deleted your email and feels no remorse."
)


def main():
    # The gate requires 1-140 characters, a single line, UTF-8 text.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
