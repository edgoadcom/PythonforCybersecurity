#!/usr/bin/env python3
# Script that performs a dictionary attack 
# against known password hashes
# Needs a dictionary file to run. Suggested to use 
# https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Ed Goad
# date: 11/1/2004

# Import necessary Python modules
import os
import sys
from passlib.hash import sha512_crypt

def test_password(hashed_password, 
    salt, plaintext_password):
    # Using the provided algorithm/salt and
    # plaintext password, create a hash
    crypted_password = sha512_crypt.using(rounds=5000).hash(
        plaintext_password, salt=salt)
    # Compare hashed_password with the just created hash
    if hashed_password == crypted_password:
        return True
    return False
    
def read_dictionary(dictionary_file):
    # Open provided dictionary file
    # and read contents into variable
    file_path = os.path.join(script_dir, dictionary_file)
    f = open(file_path, "r")
    message = f.read()
    return message

# Get current file Directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Load dictionary file and prompt for hash
password_dictionary = read_dictionary("top10.txt")
hashed_password = input("What is the hashed password? ")
hash_parts = hashed_password.split("$")
salt = hash_parts[2]

# For each password in dictionary file,
# test against hashed_password
for password in password_dictionary.splitlines():
    result = test_password(hashed_password, salt, password)
    if result:
        # If a match is found, print it and quit
        print("Match found: {0}".format(password))
        sys.exit()
# No matches found, print error and quit
print("No match found, try a different dictionary")
