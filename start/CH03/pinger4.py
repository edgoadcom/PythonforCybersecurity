#!/usr/bin/env python3
# Fourth example of pinging from Python
# By Quentin athula
# 4/22/2025

# import necessary python modules
import platform
import os

def ping_host(ip):
    # Determine the current operating system
    current_os = platform.system().lower()
    if current_os == "windows":
        # Build our ping command for windows
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        # Build our ping command for other operating systems
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    # Execute command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

# Define the prefix to begin pinging
ip_prefix = "192.168.1."

# loop from 0 - 254
for final_octet in range(254):
    # Assign IP to ping to a variable
    # Adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + str(final_octet + 1)

    # call the ping_host function and capture the return value
    exit_code = ping_host(ip)

    # print results to console only if successful
    if exit_code == 0:
        print("{0} is online" .format(ip))
