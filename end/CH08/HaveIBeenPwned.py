#!/usr/bin/env python3
# Script that checks passwords against haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Ed Goad
# date: 2/5/2021

# Import Python modules
import requests
import hashlib

def check_haveibeenpwned(sha_prefix):
    pwnd_dict = {}
    request_uri = "https://api.pwnedpasswords.com/range/" + \
        sha_prefix
    r = requests.get(request_uri)
    pwnd_list = r.text.split("\r\n")
    for pwnd_pass in pwnd_list:
        pwnd_hash = pwnd_pass.split(":")
        pwnd_dict[pwnd_hash[0]] = pwnd_hash[1]
    return pwnd_dict

password = input("What password needs to be checked? ")
sha_password = hashlib.sha1(password.encode()).hexdigest()
sha_prefix = sha_password[0:5]
sha_postfix = sha_password[5:].upper()
pwnd_dict = check_haveibeenpwned(sha_prefix)

if sha_postfix in pwnd_dict.keys():
    print("Password has been compromised {0} times".format( \
        pwnd_dict[sha_postfix]))
else:
    print("Password has not been compromised. It is safe to use!")
