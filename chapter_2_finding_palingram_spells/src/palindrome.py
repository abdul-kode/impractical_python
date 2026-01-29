"""Find Number of words and plaindromes in a dictionary file."""

import load_dictionary

def main():
    """Main function"""
    list_of_words = load_dictionary.load("words")
    palindrome = []
    number_of_words = 0

    for word in list_of_words:
        number_of_words += 1
        reverse_word = word[::-1]
        if len(word)>1 and reverse_word == word:
            palindrome.append(word)

    print(f"\nFrom {number_of_words} words, Number of palindromes found = {len(palindrome)}\n")
    print(*palindrome, sep='\n')

if __name__ == "__main__":
    main()
