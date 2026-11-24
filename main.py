import os

TEXT = (
    "A toaster is a little elevator that carries your bread down into a hot "
    "basement and brings it back up brown and crispy.\n"
    "The elevator part fits because the bread really rides down and pops "
    "back up, but the heat comes from glowing wires, not the basement, and a "
    "timer \u2014 not the bread \u2014 picks when the ride ends."
)


def main():
    assert 1 <= len(TEXT) <= 400, "gate: entry must be 1-400 characters"
    assert TEXT.count("\n") == 1, "gate: entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
