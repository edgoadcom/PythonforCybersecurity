#!/usr/bin/env python3
# Sample script that writes to a file
# By Ed Goad
# 2/27/2021

# Open file for writing
test_file = open("testfile.txt", "w")

# Write lines to the file
test_file.write("Hello World\n")
test_file.write("My name is Ed\n")
test_file.write("I like rubber ducks\n")

# Close the file
test_file.close()

