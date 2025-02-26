#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by Ed Goad, 2/3

# Get users name
your_name = input("What is your name? ")

# String formatting and f-string
print("Hello {0}".format(your_name))
print(f"Hello {your_name}")

# String concatenation
print("Hello " + your_name)

# Multiple print arguments
print("Hello", your_name)

# Constructing new variables
message = "Hello" + " " + your_name
print(message)

# Removing newline
print("Hello ", end = "")
print(your_name)

# Old style formatting
print("Hello %s" % your_name)

# Joining text
print(" ".join(["Hello", your_name]))
