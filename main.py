"""Write one original one-liner about a meeting that should have been an email.

The program writes exactly one line of plain text to entry.txt in the
output directory (OUTPUT_DIR, default /output). Pure standard library.
"""

import os

# Sharper line: the laugh lands on the last word, and it names something
# everyone who has sat through that meeting recognises.
LINE = (
    "Forty-five minutes in, someone finally said it out loud: "
    "'This meeting is just an email with catering.'"
)


def main():
    # Gate guard: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "entry line outside 1-200 char gate"
    assert LINE.strip(), "entry line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
