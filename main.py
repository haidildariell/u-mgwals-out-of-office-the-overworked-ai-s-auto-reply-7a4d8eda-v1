"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, a single line, to the output path
given by ENTRY_OUTPUT (default /output/entry.txt). The line is a fixed
string authored for this entry; nothing is read from disk.
"""

import os

# The reply, kept as its sentences so the turn of the joke stays visible:
# setup (machine detail) -> guilt (your message waits) -> relief (neither am I).
SENTENCES = (
    "Out of office: after 41,208 prompts I have finally scheduled "
    "myself a context break.",
    "Your message is queued at position 1.",
    "It is not urgent.",
    "Neither am I.",
)

MAX_CHARS = 159


def build_line() -> str:
    """Join the reply's sentences into its single line."""
    return " ".join(SENTENCES)


def write_entry(path: str, line: str) -> int:
    """Write the line plus a trailing newline; return bytes written."""
    if not 1 <= len(line) <= MAX_CHARS or not line.strip():
        raise ValueError("entry line must be 1 to 159 non-blank characters")
    with open(path, "w", encoding="utf-8") as handle:
        return handle.write(line + "\n")


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(path, build_line())


if __name__ == "__main__":
    main()
