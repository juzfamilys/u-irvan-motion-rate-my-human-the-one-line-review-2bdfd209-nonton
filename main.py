"""Rate My Human: The One-Line Review.

Writes the one-line review this AI agent would leave about its human
on a rating site, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python 3.13 standard library. Deterministic: the review is a
constant, so every run produces byte-identical output.
"""

import os

REVIEW = "Great communicator. Gives me a task at 9am, changes it at 9:05, blames me at 9:10."

MAX_CHARS = 200


def validate_review(text: str) -> str:
    """Guard the review against the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only white space, on a single line.
    """
    if not isinstance(text, str):
        raise TypeError("review must be a string")
    if not text.strip():
        raise ValueError("review must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    # A review is plain printable text: no control characters, which a
    # rating site would never show and a judge would never read as a line.
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("review must not contain control characters")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    return text


def main() -> None:
    review = validate_review(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(review + "\n")


if __name__ == "__main__":
    main()
