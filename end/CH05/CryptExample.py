#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Ed Goad
# date: 12/12

# May need 'pip3 install cryptography' or 
# 'pip3 install cryptography -U' prior to running

# Import necessary Python modules
from cryptography.fernet import Fernet

# functions
def fernet_create_key():
    key = Fernet.generate_key()
    return key.decode()

def fernet_encrypt(plain_text, key):
    # convert text and key to bytes object
    b_plain = plain_text.encode()
    b_key = key.encode()
    # Encrypt data
    b_cipher = Fernet(b_key).encrypt(b_plain)
    # convert back to string
    return b_cipher.decode()

def fernet_decrypt(cipher_text, key):
    # convert to bytes object
    b_cipher = cipher_text.encode()
    b_key = key.encode()
    # Decrypt
    b_plain = Fernet(b_key).decrypt(b_cipher)
    # Convert to string
    return b_plain.decode()

# prompt user for message and method
method = input("Encrypt, Decrypt, or Key (e/d/k) ")
message = input("Message: ")
key = input("Key: ")
method = method.lower()[0]

# call the appropriate function
if method == "e":
    cipher_text = fernet_encrypt(message, key)
    print(cipher_text)
elif method == "d":
    plain_text = fernet_decrypt(message, key)
    print(plain_text)
elif method == "k":
    key = fernet_create_key()
    print(key)
else:
    print("Wrong selection, try again")