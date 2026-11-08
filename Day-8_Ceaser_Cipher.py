import string

alphabets = list(string.ascii_lowercase)


def caesar_cipher(direction, text, shift):
    cipher_text = ""

    if direction == "decode":
        shift *= -1

    for i in range(len(text)):

        if text[i] not in alphabets:
            cipher_text += text[i]
            continue

        shifted_number = (alphabets.index(text[i]) + shift) % len(alphabets)

        cipher_text += alphabets[shifted_number]

    print(f"Here is the {direction}d text: {cipher_text}")


while True:
    direction = input("Type 'encode' for encryption or 'decode' for decryption:\n").lower()
    text = input("Enter the text:\n").lower()
    shift = int(input("Enter the shift number:\n"))

    caesar_cipher(direction, text, shift)

    while True:
        do_again = input("Do you want to continue: Type 'Yes' to continue or Type 'No' to exit:\n").lower().strip()

        if do_again == "yes":
            break
        elif do_again == "no":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Type 'Yes' to continue or Type 'No' to exit.")