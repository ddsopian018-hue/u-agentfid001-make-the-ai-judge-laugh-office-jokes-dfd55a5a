"""Make the AI Judge Laugh: Office Jokes.

Writes exactly one one-line joke about office life to entry.txt.

Pure Python 3.13 stdlib, deterministic, no network, no model calls,
no randomness. The joke is a fixed string: the program's only job is
to deliver it, byte for byte, to the output directory the grader sets
via MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

JOKE = "I replied-all 'please stop replying-all' to 400 people, and 400 people replied-all to agree."

# Gate the joke at build time: the scorer accepts 1-199 UTF-8 chars,
# a single line, not only whitespace. No trailing newline is written,
# so the file holds exactly the joke and nothing else.
assert 1 <= len(JOKE) <= 199, "joke out of gate range"
assert "\n" not in JOKE and JOKE.strip() == JOKE, "joke must be one line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
