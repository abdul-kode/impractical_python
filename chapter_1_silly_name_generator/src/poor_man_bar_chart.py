"""
Python script that takes a sentence (string) as input
and returns a simple bar chart–type to show which letter is used how many times.

Example of the book: Like the castle in its corner in a medieval game,
I foresee terrible trouble and I stay here just the same.
"""

from collections import defaultdict
import re
from pprint import pprint

def user_input_str():
    """Taking input from user and return that string."""

    raw_sentence = input("Enter the setence: ")
    return raw_sentence

def clean_data(raw_text: str) -> str:
    """Remove non-alphabetic characters and normalize to lowercase."""

    return re.sub(r"[^a-zA-Z]", "", raw_text.lower())

def build_bar_chart(text: str) -> str:
    """Analyze text and return a dictionary mapping letters to a list of those letters."""
    chart = defaultdict(list)
    for letter in text:
        chart[letter].append(letter)
    return chart

def main():
    """Main execution flow."""

    raw_input = user_input_str()

    clean_text = clean_data(raw_input)
    analysis_result = build_bar_chart(clean_text)

    # Display logic
    print("\n--- Letter Bar Chart ---")
    pprint(analysis_result, width=120, compact=True)

if __name__ == "__main__":
    main()
