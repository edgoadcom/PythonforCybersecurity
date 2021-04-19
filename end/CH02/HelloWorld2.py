#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by Ed Goad, 2/3/2021

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

yourName = input("What is your name? ")
print("Hello {0}".format(yourName))
print(f"Hello {yourName}")
print("Hello " + yourName)
print("Hello", yourName)
message = "Hello" + " " + yourName
print(message)