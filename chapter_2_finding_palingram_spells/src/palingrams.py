"""Find plaingrams and number of words from a dictionary file."""

import load_dictionary

def find_palingrams(words: list) -> list:
    """Find palingrams and number of words."""
    palingrams = []
    number_of_words = 0

    for word in words:
        number_of_words += 1
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[:end-i] in words:
                    palingrams.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[end-i:] in words:
                    palingrams.append((rev_word[:end-i], word))

    return palingrams, number_of_words

def main():
    """Main function"""
    list_of_words = load_dictionary.load("words")

    paligrams_list, number_of_words = find_palingrams(list_of_words)
    paligrams_sorted = sorted(paligrams_list)

    print(f"\nFrom {number_of_words} words, Number of palindromes found = {len(paligrams_list)}\n")
    for first, second in paligrams_sorted:
        print(f"{first} {second}")



if __name__ == "__main__":
    main()
