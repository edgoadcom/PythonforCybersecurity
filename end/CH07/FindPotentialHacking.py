#!/usr/bin/env python3
# Script that scans web server logs for possible hacking
# Use RegEx to find and report on common hacking types
# Based on 
# https://www.cgisecurity.com/fingerprinting-port-80-attacks-a-look-into-web-server-and-web-application-attack-signatures.html
# and
# https://www.cgisecurity.com/fingerprinting-port80-attacks-a-look-into-web-server-and-web-application-attack-signatures-part-two.html
# By Ed Goad
# date: 2/5/2021

#Import Python modules
import os
import re

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Get current file Directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, log_file)

# Open file and load into memory
with open(file_path, "r") as f:
    sample_logs = f.readlines()

# Setup regex patterns
request_start = r'"\w+ ([^"]*'
request_end = r'[^"]*) HTTP\/\d\.\d"'
find_wildcard_uri_pattern = request_start + r'\*' + request_end
find_backtick_uri_pattern = request_start + r'`' + request_end
find_code_uri_pattern = request_start + r'[\^\[\]#{}\"]' + request_end
find_css_uri_pattern = request_start + r'[\(\)]' + request_end
find_foldertraversal_uri_pattern = request_start + r'\.{2,}' + request_end

# Find match and report
for line in sample_logs:
    # Search for pattern, and if found move forward
    m = re.search(find_wildcard_uri_pattern, line)
    if m:
        print("Possible attack: Wildcard in URI")
        print("\t{0}".format(line.strip()))
    m = re.search(find_backtick_uri_pattern, line)
    if m:
        print("Possible attack: Backtick (`) in URI")
        print("\t{0}".format(line.strip()))
    m = re.search(find_code_uri_pattern, line)
    if m:
        print("Possible attack: Code in URI")
        print("\t{0}".format(line.strip()))
    m = re.search(find_css_uri_pattern, line)
    if m:
        print("Possible attack: Potential CSS in URI")
        print("\t{0}".format(line.strip()))
    m = re.search(find_foldertraversal_uri_pattern, line)
    if m:
        print("Possible attack: Folder Traversal in URI")
        print("\t{0}".format(line.strip()))

