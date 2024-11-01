#!/usr/bin/env python3
# Script that hashes a password with provided salt
# By Ed Goad
# date: 11/1/2024

# Import Python modules
from passlib.hash import sha256_crypt
from passlib.hash import sha512_crypt

# Prompt user for plain-text password
plain_password = input("What is the password? ")
salt = input("What is the salt? ")

# Print out hashes
print("SHA-256      : {0}".format(
    sha256_crypt.hash(plain_password, salt=salt))
    )
print("SHA-512      : {0}".format(
    sha512_crypt.hash(plain_password, salt=salt))
    )

