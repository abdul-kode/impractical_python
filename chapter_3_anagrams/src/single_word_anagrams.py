"""Finding anagrams of a word using dictionary"""

import load_dictionary

words = load_dictionary.global_data("words")
print(words)

def main():
    anagram_list = []

    user_word = input("Enter a word to find anagrams: ")
    user_word = user_word.lower()
    sorted_word = sorted(user_word)

    for anagram in words:
        anagram = anagram.lower()
        if anagram != user_word:
            if sorted(anagram) == sorted_word:
                anagram_list.append(anagram)

    if len(anagram_list) == 0:
        print("You need a larger dictionary or another name")

    else:
        print("Anagrams = ", *anagram_list, sep='\n')



if __name__ == "__main__":
    main()
