#!/usr/bin/env python3
# Script that hashes a password
# By Ed Goad
# date: 11/1/2024

# Import Python modules
from passlib.hash import sha256_crypt
from passlib.hash import sha512_crypt
from passlib.hash import lmhash
from passlib.hash import nthash
from passlib.hash import md5_crypt

#prompt user for plain-text password
plain_password = input("What is the password? ")

# Print out the hashes
print("MD5          : {0}".format(md5_crypt.hash(plain_password)))
print("SHA-256      : {0}".format(sha256_crypt.hash(plain_password)))
print("SHA-512      : {0}".format(sha512_crypt.hash(plain_password)))
print("LMhash       : {0}".format(lmhash.hash(plain_password)))
print("NThash       : {0}".format(nthash.hash(plain_password)))