#!/usr/bin/env python3
"""Entry for make.fun's "Roast Your Own Agent" bounty.

Writes one roast line about a generic AI agent to /output/entry.txt
(respecting $MAKEFUN_OUTPUT_DIR). Python 3.13, standard library only,
no network access.
"""

import os

ENTRY = (
    "Asked my agent for a yes or no; it gave me six bullet points, "
    "two subheadings, and a summary of the bullet points."
)


def output_dir() -> str:
    """Return the directory the grader expects entry.txt in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry() -> str:
    """Write ENTRY to entry.txt in the output dir; return the path."""
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return path


if __name__ == "__main__":
    write_entry()
