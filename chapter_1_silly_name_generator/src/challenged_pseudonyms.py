"""
This script generates random, funny, and cool pseudonyms.
But this time more advance one as we have option of
by combining randomly chosen first, last names and __middle name__.
"""

import random
import sys
from pathlib import Path

def load_names(filename: str):
    """
    Read a text file and return a list of names.

    Uses Pathlib for professional path handling.
    """
    data_path = Path(__file__).parent.parent/ "data" /filename

    try:
        with open(data_path, 'r', encoding="utf-8") as f:
            names = f.read().splitlines()

        if not names:
            raise ValueError(f"{filename} is empty")

        return names

    except FileNotFoundError:
        print(f"Error: The file {filename} not found at {data_path}", file=sys.stderr)
        sys.exit(1)

def generate_silly_name(first: list[str], last: list[str], middle: list[str]) -> str:
    """
    Randomly choosing words from three list and return it as a string.
    The middle will be only used one third time
    """
    chance = random.randint(1, 3)

    if chance < 2:
        return f"{random.choice(first)} {random.choice(last)}"

    return f"{random.choice(first)} {random.choice(middle)} {random.choice(last)}"


if __name__=="__main__":
    first_list = load_names("first_names.txt")
    last_list = load_names("last_names.txt")
    middle_list = load_names("middle_names.txt")
    print("\n--- Welcome to the Silly Name Generator---\n")

    while True:
        print("\n", generate_silly_name(first_list, last_list, middle_list))

        try_again = input("Try again? Press Enter else exi to quite: -> ")
        if try_again.lower() == "exi":
            break

    input("\nPress Enter to exit.")
