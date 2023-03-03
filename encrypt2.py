import string
import random

def generate_key():
    #function that generates a random key 
    key = ""
    for i in range(26):
        alphabet = list(string.ascii_lowercase)
        random.shuffle(alphabet)
        key += "".join(alphabet)
    return key

def encrypt(plaintext, key):
    #function that encrypts plaintext using polyalphabetic substitution cipher rules
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i % 26]) - ord('a')
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += plaintext[i]
    return ciphertext

# generate a key
key = generate_key()

    # encrypt input plaintext
plaintext = input("What do you want encrypted? ") 
ciphertext = encrypt(plaintext, key)
print("Your (psc) ecrypted text is:", ciphertext)
print("Key:",key )
print("* you can use your specfic key to decrypt your text more accurately*")
