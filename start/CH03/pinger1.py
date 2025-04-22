#!/usr/bin/env python3
# First example of pinging from Python
# By Quentin Athula
# 4/22/2025

# import necessary python modules
import platform
import os

# Assign IP address to ping to a variable
ip = "127.0.0.1"
# Build the command to ping the IP address
ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
# Execute command and capture exit code
exit_code = os.system(ping_cmd)
# print the result to the console
print(exit_code)