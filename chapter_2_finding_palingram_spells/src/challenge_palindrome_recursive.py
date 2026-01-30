"""Find Number of words and plaindromes in a dictionary file but this time Recursively."""

import load_dictionary

def is_palindrome(word: str) -> bool:
    """Check if a word is palindrome or not using recursion"""

    if len(word) <= 1:
        return True

    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])

    return False


def main():
    """Main function"""
    list_of_words = load_dictionary.load("words")
    palindrome = []
    number_of_words = 0

    for word in list_of_words:
        number_of_words += 1
        if len(word) != 1 and is_palindrome(word):
            palindrome.append(word)

    print(*palindrome, sep='\n')
    print(f"\nFrom {number_of_words} words, Number of palindromes found = {len(palindrome)}\n")

if __name__ == "__main__":
    main()
