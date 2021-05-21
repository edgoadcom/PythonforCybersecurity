#!/usr/bin/env python3
# Fourth example of pinging from Python
# By Ed Goad
# 2/27/2021

# import necessary Python modules
import platform
import os

def ping_host(ip):
    # Determine the currrent OS
    currrent_os = platform.system().lower()
    if currrent_os == "windows":
        # Build our ping command for Windows
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        # Build our ping command for other OSs
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    # Execute command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

# Define the prefix to begin pinging
ip_prefix = "192.168.0."

# Loop from 0 - 254
for final_octet in range(254):
    # Assign IP to ping to a variable
    # Adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + str(final_octet + 1)
    
    # Call ping_host function and capture the return value
    exit_code = ping_host(ip)

    # Print results to console only if successful
    if exit_code == 0:
        print("{0} is online".format(ip))
