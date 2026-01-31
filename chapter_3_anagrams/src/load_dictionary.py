"""Load a text file as list.

Arguments:
    - text file name

Exceptions:
    - IOError is filename not found

Return:
    - A list of all words in a text file in lower case and cleaned from
        single words other than 'a' and 'i'

Require:
    - import sys
    - import Path

"""
import sys
from pathlib import Path

def load(filename: str) -> list:
    """Load dictionary from data directory and return the words in a list form."""

    dir_path = Path(__file__).parent.parent.parent/ "data"
    words_path = dir_path / filename

    permissible = ('a', 'i')

    try:
        with open(words_path, "r", encoding="utf-8") as f:
            words = f.read().strip().split("\n")
            words_list = []

            for word in words:
                if len(word) == 1 and word not in permissible:
                    continue

                words_list.append(word)

        if not words_list:
            raise ValueError("file is empty")

        return words_list

    except FileNotFoundError:
        print("Error: The file not found", file=sys.stderr)
        sys.exit(1)
