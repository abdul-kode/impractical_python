"""
This program is used to form pig latin words.
It will simply take a word and will convert it to pig latin
"""

def pig_latin(word: str) -> str:
    """
    Convert a single English word to Pig Latin.
    Consonant clusters are moved to the end.
    """

    word = word.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}

    if not word:
        return ""

    if word[0] in vowels:
        return f"{word}way"

    for i, letter in enumerate(word):
        if letter in vowels:
            return f"{word[i:]}{word[:i]}ay"

    # with no vowels
    return f"{word}ay"

def main():
    """Entry point for the Pig Latin converter."""
    user_input = input("Enter the words: ").split()

    pig_latin_words = [pig_latin(w) for w in user_input]

    print(f"Pig Latin equivalent is: {" ".join(pig_latin_words)}")


if __name__ == "__main__":
    main()
