"""Load a text file as list.

Arguments:
    - text file name

Exceptions:
    - IOError is filename not found

Return:
    - Alist of all words in a text file in lower case

Require:
    - import sys
    - import Path

"""
import sys
from pathlib import Path

def load(filename: str) -> list:
    """Load dictionary from data directory and return the words in a list form."""

    dir_path = Path(__file__).parent.parent/ "data"
    words_path = dir_path / filename
    try:
        with open(words_path, "r", encoding="utf-8") as f:
            words = f.read().strip().split("\n")
            words = [x.lower() for x in words]
        if not words:
            raise ValueError("file is empty")
        return words

    except FileNotFoundError:
        print("Error: The file not found", file=sys.stderr)
        sys.exit(1)
