#!/usr/bin/env python3
# Script that hashes a password
#By Ed Goad
# date: 2/5/2021
import crypt

# Simple script that takes an unhashed password and a salt
# We then hash the password + salt using various types

# Sample data
# Password: Password01
# Salt: G.DTW7g9s5U7KYf5
# SHA-512 result: 
# $6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.

plainPass = input("What is the password? ")
salt = input("What is the salt? ")
print("MD5       : {0}".format(crypt.crypt( \
    plainPass,"$1$" + salt)))
print("Blowfish  : {0}".format(crypt.crypt( \
    plainPass,"$2$" + salt)))
print("eksblofish: {0}".format(crypt.crypt( \
    plainPass,"$2a$" + salt)))
print("SHA-256   : {0}".format(crypt.crypt( \
    plainPass,"$5$" + salt)))
print("SHA-512   : {0}".format(crypt.crypt( \
    plainPass,"$6$" + salt)))

