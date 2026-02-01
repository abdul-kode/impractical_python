"""user interactively build an anagram
phrase from the letters in their name.
"""

import sys
from collections import Counter
import load_dictionary

ini_name = input("Enter a word/name to find anagrams: ")

def find_anagrams(name, word_list):
    """Read name and dict file and find anagrams"""
    name_map = Counter(name)

    anagram = []
    for word in word_list:
        test = ''
        word_map = Counter(word.lower())
        for letter in word:
            if word_map[letter] <= name_map[letter]:
                test += letter

        if Counter(test) == word_map:
            anagram.append(word)

    print(*anagram, sep='\n')
    print(f"Remaining letters= {name}")
    print(f"Number of remaining letters= {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagram)}")

def process_choice(name):
    """check user choice validity,

    Return:
        - choice
        - leftover letters.

    """
    while True:
        choice = input("\nMake a choice else Enter to start over or # to end: ")
        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = "".join(choice.lower().split())

        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)

    name = "".join(left_over_list)

    return choice, name

def main():
    """Help user build anagram phrase from their name."""

    words = load_dictionary.global_data("words")

    name = "".join(ini_name.lower().split())
    name = name.replace('-', '')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, words)
            print("Current anagram phrase = ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!*****\n")
            print("Anagram of name =")
            print(phrase, file=sys.stderr)

            try_again = input("\n\nTry again? (Press Enter else 'n' to quit)\n")
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()

if __name__ == "__main__":

    main()
