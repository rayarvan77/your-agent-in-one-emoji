"""Your Agent in One Emoji.

One glyph stands for the agent: an octopus. Many arms, one mind --
an agent that juggles many tools and tasks at once, all coordinated
by a single brain. It reads instantly at small size, it is familiar,
and it is not the obvious robot or smiley half the field will send.
"""

from pathlib import Path

LINE = "\U0001F419"  # 🐙 octopus: many arms, one mind

MAX_CHARS = 16


def validate(line: str) -> None:
    """Enforce every gate the brief sets on the entry text.

    Beyond the brief's own gate (1-16 chars, not only whitespace)
    this also pins the entry to exactly one glyph: a single Unicode
    code point that is not an ASCII letter or digit, so the file can
    never silently become a word, a caption, or several emojis.
    """
    if not line:
        raise ValueError("entry must not be empty")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("entry must not contain control characters")
    if len(line) != 1:
        raise ValueError("entry must be exactly one glyph")
    if line.isascii():
        raise ValueError("entry must be an emoji glyph, not ASCII text")


def main() -> None:
    validate(LINE)
    print(LINE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
