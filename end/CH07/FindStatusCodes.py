#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Ed Goad
# date: 12/16

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

# Setup regex pattern and empty dictionary
status_pattern = r'\s(\d{3})\s'
statusdict = {}

# Find match and store in dictionary
for line in sample_logs:
    # Search for pattern, and if found move forward
    m = re.search(status_pattern, line)
    if m:
        result = m.group(1)
        # Put access frequency in dictionary
        if result in statusdict.keys():
            statusdict[result] += 1
        else:
            statusdict[result] = 1

# Sort by most frequently accessed
for w in sorted(statusdict, key=statusdict.get, reverse=False):
    print(w, statusdict[w])
