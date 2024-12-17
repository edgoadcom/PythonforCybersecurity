#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Ed Goad
# date: 12/16

import os

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Get current file Directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, log_file)

# Open file
f = open(file_path, "r")

# Read file line by line
while True:
    line = f.readline()
    if not line:
        break
    # Check for 404
    if "404" in line:
        print(line.strip())

# Close file
f.close()
