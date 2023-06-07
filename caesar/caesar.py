import string, sys
from julius import julius
alphabet = list(string.ascii_lowercase)
print(julius)

def main():
    type = input("Would you like to encrypt or decrypt some text(e/d)?\n").lower()
    text = input("What text would you like to use?\n").lower() # How could we implement this for capitals?
    shift = int(input("What is your shift?\n"))

    while type not in ["e", "d"]:
        print("Invalid input")
        type = input("Would you like to encrypt or decrypt some text(e/d)?\n").lower()
    caesar(text, shift, type)

def caesar(text, shift, type):
    output = ""
    if type == "d":
        shift *= -1
    for letter in text:
        if letter.isalpha():
            position = alphabet.index(letter)
            position += shift
            position %= len(alphabet)
            output += alphabet[position]
        elif letter == " ":
            output += " "
    if type == "d":
        print(f"Your decrypted text is: {output}")
    elif type == "e":
        print(f"Your encrypted text is: {output}")

if __name__ == "__main__":
    start = input("Would you like to use the cipher(y/n)?\n").lower()
    while start != "n":
        main()
        start = input("Would you like to use the cipher again(y/n)?\n").lower()
    print("Thanks for using the cipher!\nGoodbye!")
    print(julius)
    print("Veni Vidi Vici")
    sys.exit(1)
