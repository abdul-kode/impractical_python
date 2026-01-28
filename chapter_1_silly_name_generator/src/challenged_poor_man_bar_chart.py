"""
Python script that takes a sentence (string) as input
and returns a simple bar chart–type to show which letter is used how many times.

Example of the book (default): Like the castle in its corner in a medieval game,
I foresee terrible trouble and I stay here just the same.
"""

from collections import defaultdict
import re
from pprint import pprint
from pathlib import Path
import string
import sys

def user_input_str():
    """
    Taking input from user and return two string, one is in english language and
    other one in any other latin-based language.
    """

    choice = input("1. Enter sentence\n2. Use default sentence\n\nSelect 1 or 2: ")
    if choice == "1":
        eng = input("Enter the setence in english: ")
        foreign = input("Enter in any other latin-based language: ")
        return eng, foreign

    # to ignore any error we are just using else so if the user enter anything we will use default sentence
    data_dir = Path(__file__).parent.parent/ "data"
    eng_path =  data_dir / "text.txt"
    foreign_path = data_dir / "foreign_text.txt"

    try:
        with open(eng_path, "r", encoding="utf-8") as f:
            text = f.read()
        with open(foreign_path, "r", encoding="utf-8") as f2:
            foreign_text = f2.read()
        if not text and foreign_text:
             raise ValueError("file is empty")
        return (" ".join(text), " ".join(foreign_text))
    except FileNotFoundError:
        print("Error: The file not found", file=sys.stderr)
        sys.exit(1)

def clean_data(raw_text: str, raw_foreign_text: str) -> tuple:
    """Remove non-alphabetic characters and normalize to lowercase."""

    CLEAN_PATTERN = re.compile(r"[^a-z]")
    clean_text = CLEAN_PATTERN.sub("", raw_text.lower())
    clean_foreign_text = CLEAN_PATTERN.sub("", raw_foreign_text.lower())

    return (clean_text, clean_foreign_text)

def build_bar_chart(text: str, foreign: str) -> defaultdict:
    """Analyze text and return a dictionary mapping letters to a list of those letters."""
    chart = defaultdict(list)

    # to initalize all the alphabets in dict
    for letter in string.ascii_lowercase:
        chart[letter] = [0, 0]

    def count_letters(source: str, index: int):
        for char in source:
            chart[char][index] += 1

    count_letters(text, 0)
    count_letters(foreign, 1)

    return chart

def main():
    """Main execution flow."""

    raw_input_eng, raw_input_foreign = user_input_str()

    clean_text, clean_forigen_text = clean_data(raw_input_eng, raw_input_foreign)
    analysis_result = build_bar_chart(clean_text, clean_forigen_text)

    # Display logic
    # 3. Present
    print("\n" + "="*40)
    print(f"{'Letter':<10} | {'English':<10} | {'Foreign':<10}")
    print("-" * 40)
    pprint(analysis_result, width=120, compact=True)

if __name__ == "__main__":
    main()
