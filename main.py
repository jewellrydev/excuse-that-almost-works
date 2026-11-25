"""The Excuse That Almost Works — a make.fun entry.

Prints exactly one line of plain text, at most 20 words, that reads
like something a real person would send in a hurry.
"""

LINE = "Sorry I'm late — my alarm and I had a disagreement, and it won on a technicality called snooze."


def build_line() -> str:
    line = LINE
    assert len(line.split()) <= 20, f"too many words: {len(line.split())}"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
