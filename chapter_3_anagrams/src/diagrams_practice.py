"""This script is used to find diagrams of a word and
also their frequency of occurace in the whole dictionary.
"""

import re
from itertools import permutations
from collections import defaultdict
import load_dictionary

def find_diagram(name: str) -> set:
    """
    Action:
        Every possible combination of a letter.
        loop through each permutation and find diagrams of it.

    Return:
        a set of digrams of the given name.
    """
    perms = {"".join(x) for x in permutations(name)}
    digrams = set()

    for perm in perms:
        for i in range(0, len(perm) - 1 ):
            digrams.add(perm[i] + perm[i+1])

    return digrams

def count_diagram(digrams: set, words_list: list) -> defaultdict:
    """count the frequency of occurance of given diagrams in given list"""
    digrams_in_dictionary = defaultdict(int)
    for word in words_list:
        word = word.lower()
        for digram in digrams:
            for _ in re.finditer(digram, word):
                digrams_in_dictionary[digram] += 1

    return digrams_in_dictionary

def main():
    """Calling functions and printout the required output."""

    words_list = load_dictionary.global_data("words")

    name = "tmvoordle"
    name = name.lower()

    digrams = find_diagram(name)

    print(*sorted(digrams), sep="\n")
    print(f"\nNumber of digrams = {len(digrams)}\n")

    digram_map = count_diagram(digrams, words_list)

    print("digram frequecny count: ")
    count = 0
    for i in sorted(digram_map):
        print(f"{i} {digram_map[i]}")


if __name__ == "__main__":
    main()
