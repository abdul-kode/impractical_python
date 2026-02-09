plaintext = "Let us cross over the river and rest under the shade of the trees"

def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespace."""
    message = "".join(plaintext.split())
    message = message.upper()  # convention for ciphertext is uppercase
    print(f"\nplaintext = {plaintext}")
    return message

def build_rails(message):
    """Build strings with every other letter in a message."""
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails

def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make string."""
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print(f"ciphertext = {ciphertext}")

def main():
    """Run program to encrypt message."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


if __name__ == '__main__':
    main()
