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

def decrypt(ciphertext, key):
    #function that decrypt ciphertext using polyalphabetic substitution cipher rules
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i % 26]) - ord('a')
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                plaintext += chr((ord(ciphertext[i]) - ord('a') - shift + 26) % 26 + ord('a'))
        else:
            plaintext += ciphertext[i]
    return plaintext

# generate a key
key = generate_key()

# retrieve specific key and decrypt input ciphertext
key = input("What is the (psc) specific key? ")
ciphertext = input("What do you want decrypted? ")
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)

