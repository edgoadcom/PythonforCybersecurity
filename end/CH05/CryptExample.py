#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Ed Goad
# date: 2/5/2021

# May need 'pip3 install cryptography' or 
# 'pip3 install cryptography -U' prior to running
# Import necessary Python modules
from cryptography.fernet import Fernet

def create_key():
    # Generate an encryption key
    # Keep this key secret and store in a secure location
    key = Fernet.generate_key()
    print("Key:", key.decode())

def encrypt(plain_text, key):
    # Convert plain_text and key into bytes for encryption
    plain_text = plain_text.encode()
    key = key.encode()
    # Encrypt the data using the provided key
    cipher_text = Fernet(key).encrypt(plain_text)
    # Convert the cipher_text back to a string
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(cipher_text, key):
    # Convert cipher_text and key into bytes
    cipher_text = cipher_text.encode()
    key = key.encode()
    # Decrypt the data using the provided key
    plain_text = Fernet(key).decrypt(cipher_text)
    # Convert plain_text back to a string
    plain_text = plain_text.decode()
    return plain_text

encKey = ""
# Prompt the user for the method to use
print("Which would you like to do: ")
method = input("Create key, Encrypt, Decrypt (c/e/d)? ")
method = method[0].lower()
# Using the first letter of method, call the correct functions
if method == "c":
    create_key()
elif method == "e":
    # Prompt user for plain_text message and encryption key
    plain_text = input("Message to encrypt: ")
    encKey = input("Encryption key: ")
    # Call the encryption function and print the results
    cipher_text = encrypt(plain_text, encKey)
    print(cipher_text)
elif method == "d":
    # Prompt user for cipher_text message and encryption key
    cipher_text = input("Message to decrypt: ")
    encKey = input("Encryption key: ")
    # Call the decryption function and print the results
    plain_text = decrypt(cipher_text, encKey)
    print(plain_text)
else:
    # Invalid choice was selected, print error and quit
    print("Wrong selection, choose C, E, or D")
