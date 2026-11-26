#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, to /output/entry.txt: the line the
writer would send back to their younger self if one line were all they got.
"""
import os

ENTRY = "Keep the Rp 5.000 on Friday — the noodles are gone by midnight, but the bus home is the last dinner you'll ever eat at your mother's table."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
