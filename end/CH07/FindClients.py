#!/usr/bin/env python3
# Script that scans web server logs for client addresses
# Use RegEx to find and report on most frequent users
# By Ed Goad
# date: 2/5/2021

#Import Python modules
import re

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Open file and load into memory
with open(log_file, "r") as f:
    sample_logs = f.readlines()

# Setup regex pattern and empty dictionary
client_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
clientdict = {}

# Find match and store in dictionary
for line in sample_logs:
    # Search for pattern, and if found move forward
    m = re.search(client_pattern, line)
    if m:
        client = m.group()
        # Put access frequency in dictionary
        if client in clientdict.keys():
            clientdict[client] += 1
        else:
            clientdict[client] = 1


# Sort by most frequently accessed
for w in sorted(clientdict, key=clientdict.get, reverse=False):
    print(w, clientdict[w])
