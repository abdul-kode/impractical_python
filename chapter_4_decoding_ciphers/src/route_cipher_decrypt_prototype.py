"""A prototype decryption script. This script will decrypt a route cipher."""

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
cipher_list = ciphertext.split()

columns = 4
rows = 5
key_initial = "-1,2,-3,4"
key_initial = key_initial.split(",")

translation_matrix = [None] * columns
plain_text = ""

start = 0
stop = rows
for key in key_initial:
    key = int(key)
    if key < 0:
        col_items = cipher_list[start:stop]
    elif key > 0:
        col_items = list(reversed(cipher_list[start:stop]))

    translation_matrix[abs(key)-1] = col_items
    start += rows
    stop += rows

print(f"\nciphertext = {ciphertext}")
print("\ntranslation matrix =", *translation_matrix, sep="\n")
print(f"\nkey length= {len(key_initial)}")

for i in range(rows):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plain_text += word + ' '

print(f"\nplaintext = {plain_text}")
