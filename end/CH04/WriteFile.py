#!/usr/bin/env python3
# Sample script that writes to a file
# By Ed Goad
# 12/12

import os

# Get current file directory
script_path = os.path.abspath( __file__ )
script_dir = os.path.dirname( script_path )
# Build file path
file_path = os.path.join(script_dir, "testfile.txt")

# Open file for writing
test_file = open(file_path, "w")

# Write lines to the file
test_file.write( "Hello World\n" )
test_file.write( "My name is Ed\n" )
test_file.write( "I like rubber ducks\n" )

# Close the file
test_file.close()

