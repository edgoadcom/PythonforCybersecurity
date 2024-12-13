#!/usr/bin/env python3
# Sample script that reads from a file
# By Ed Goad
# 12/12

import os

# Get current file directory
script_path = os.path.abspath( __file__ )
script_dir = os.path.dirname( script_path )
# Build file path
file_path = os.path.join(script_dir, "ips.txt")

# Open file for reading
ip_file = open(file_path, "r")

# Read the contents of the file and print to screen
ip_addresses = ip_file.read()
print(ip_addresses)

# Close the file
ip_file.close()

