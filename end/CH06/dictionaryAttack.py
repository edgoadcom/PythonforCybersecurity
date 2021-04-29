#!/usr/bin/env python3
# Script that performs a dictionary attack 
# against known password hashes
# Needs a dictionary file to run. Suggested to use 
# https://github.com/danielmiessler/SecLists
# /tree/master/Passwords/Common-Credentials
# By Ed Goad
# date: 2/5/2021

# Import necessary Python modules
import crypt

def test_password(hashed_password, \
    algorithm_salt, plaintext_password):
    # Using the provided algorithm/salt and
    # plaintext password, create a hash
    crypted_password = crypt.crypt( \
        plaintext_password, algorithm_salt)
    # Compare hashed_password with the just created hash
    if hashed_password == crypted_password:
        return True
    return False
    

def read_dictionary(dictionary_file):
    # Open provided dictionary file
    # and read contents into variable
    f = open(dictionary_file, "r")
    message = f.read()
    return message

# Load dictionary file and prompt for hash and algorithm/salt
password_dictionary = read_dictionary("top10.txt")
hashed_password = input("What is the hashed password? ")
algorithm_salt = input("What is the algorithm and salt? ")

# For each password in dictionary file,
# test against hashed_password
for password in password_dictionary.splitlines():
    result = test_password(hashed_password, \
        algorithm_salt, password)
    if result:
        # If a match is found, print it and quit
        print("Match found: {0}".format(password))
        break
