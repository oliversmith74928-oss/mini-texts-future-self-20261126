"""Texts From Your Future Self - make.fun entry.

Writes one funny text message from the writer's future self to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only. Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    # One fixed message: no randomness, no time, no input, so every run
    # produces byte-identical output.
    "It's me, you, from 2041. The sourdough starter you keep forgetting "
    "has its own chair at dinner now. Feed it. Also stop buying plants "
    "\u2014 they unionized."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
