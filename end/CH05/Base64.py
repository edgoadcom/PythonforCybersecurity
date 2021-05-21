#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Ed Goad
# 2/5/2021

# import necessary Python modules
import base64

def encode_data(plain_text):
    # Convert plain_text string to bytes
    plain_text = plain_text.encode()
    # Encode the plain_text
    cipher_text = base64.b64encode(plain_text)
    # Convert the encoded bytes back to string
    cipher_text = cipher_text.decode()
    return cipher_text

def decode_data(cipher_text):
    # Decode the cipher_text
    plain_text = base64.b64decode(cipher_text)
    # Convert the decoded bytes to string
    plain_text = plain_text.decode()
    return plain_text

# Prompt the user for method and message
method = input("Do you wish to Encode or Decode (e/d)? ").lower()
message = input("What is the message? ")

# Using first letter in variable, 
# call the encode or decode function
if method[0] == "e":
    print(encode_data(message))
elif method[0] == "d":
    print(decode_data(message))
else:
    # if method wasn't "e" or "d", print error message and quit
    print("Wrong method selected. Choose Encode or Decode")
