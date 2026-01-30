"""REmove single-letter words from list if not 'a' or 'i'."""

word_list = ['a', "nurses", 'i', "stack", 'b', "cats", 'c']
print(f"\nRaw Word List: {word_list}")

permissible = ('a', 'i')

# remove single-letter
for word in word_list:
    if len(word) == 1 and word not in permissible:
        word_list.remove(word)

print(f"Clean Word List: {word_list}\n")
