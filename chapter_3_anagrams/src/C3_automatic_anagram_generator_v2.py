"""program automatically build an anagram
phrase from the letters the user provide.
"""

import sys
from collections import Counter
import load_dictionary

ini_name = input("Enter a word/name to find anagrams: ")
phrase_anagrams = []

def find_anagrams(name, word_list):
    """Read name and dict file and find anagrams and return it."""
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


    return anagram

def anagram_phrases(anagrams: str, name, phrase: str):
    if sum(name.values()) == 0:
        phrase_anagrams.append(phrase)
        return

    if len(phrase_anagrams) == 500:
        return

    for word in anagrams:
        word_count = Counter(word.lower())
        if word_count <= name:
            remaining_letters = name - word_count
            new_phrase = phrase + " " + word

            anagram_phrases(anagrams, remaining_letters, new_phrase)

def main():
    """Help user build anagram phrase from their name."""

    words = load_dictionary.global_data("words")

    name = "".join(ini_name.lower().split())
    name = name.replace('-', '')
    name = Counter(name)

    anagrams = find_anagrams(name, words)

    phrase = ""
    anagram_phrases(anagrams, name, phrase)

    for i in phrase_anagrams:
        print(i)



if __name__ == "__main__":

    main()
