#!/usr/bin/env python3
# Sample script that reads from a file
# By Ed Goad
# 2/27/2021

# Open file for reading
ip_file = open("ips.txt", "r")

# Read the contents of the file and print to screen
ip_addresses = ip_file.read()
print(ip_addresses)

# Close the file
ip_file.close()

