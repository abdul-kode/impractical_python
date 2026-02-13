"""

Solving cryptogram:
    input = THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY
    AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM
    CAN UP

    return: decrypted form of the cipher.

"""

import sys

ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY
AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM
CAN UP"""

# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix:
ROWS = 6

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = """ -1 2 -3 4 """

def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    len_cipher = len(cipherlist)
    if ROWS * COLS != len_cipher:
        print(f"Error: {ROWS}x{COLS} doesn't match length {len_cipher}")
        sys.exit(1)

def key_to_int(key):
    """Turn key into list of integers & check validity."""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
        or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """Turn every n-items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    for k in key_int:
        column_index = abs(k) - 1
        stop = start + ROWS
        column_data = cipherlist[start:stop]

        # If the key is positive, the route went DOWN, so the first word
        # in the cipherlist is the TOP of the column.
        # If the key is negative, the route went UP, so the first word
        # in the cipherlist is the BOTTOM of the column.
        if k < 0:
            # We want to store everything so the 'Top' is at index 0
            # If it was read UP, the first word we hit was the bottom.
            # So we reverse it to keep index 0 as the 'Top'.
            column_data.reverse()

        translation_matrix[column_index] = column_data
        start += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = []
    for i in range(ROWS):
        for matrix_col in range(COLS):
            word = translation_matrix[matrix_col][i]
            plaintext.append(word)
    return " ".join(plaintext)

def main():
    """Run program and print decrypted plaintext."""
    print(f"\nCiphertext = {ciphertext}")
    print(f"Trying {COLS} columns")
    print(f"Trying {ROWS} rows")
    print(f"Trying key = {key}")

    # split elements into words, not letters
    cipherlist = ciphertext.split()

    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f"Plaintext = {plaintext}")
    print()

if __name__ == '__main__':
    main()
