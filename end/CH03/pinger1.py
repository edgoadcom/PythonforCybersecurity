#!/usr/bin/env python3
# First example of pinging from Python
# By Ed Goad
# 2/27/2021

# import necessary Python modules
import platform
import os

# Assign IP to ping to a variable
ip = "127.0.0.1"
# Build our ping command
ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
# Execute command and capture exit code
exit_code = os.system(ping_cmd)
# Print results to console
print(exit_code)
