"""One Letter for Your Day — entry: Z.

One letter, the whole day: Z — zombie, zonked, zilch.
Zero sleep, zero energy, zero filter — the day in one letter.
"""

import os

ENTRY = "Z"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # Write exactly the entry letter: no trailing newline, no extra text.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
