#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
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

def import_addresses():
    # Create empty list object
    lines = []
    # Open file and read line-by-line
    f = open("ips.txt", "r")
    for line in f:
        # Use strip() to remove spaces and carriage returns
        line = line.strip()
        # Add the line to the lines list object
        lines.append(line)
    # Return the list object to the main body
    return lines

# read IPs from file
ip_addresses = import_addresses()

for ip in ip_addresses:    
    # Call ping_host function and capture the return value
    exit_code = ping_host(ip)

    # Print results to console only if successful
    if exit_code == 0:
        print("{0} is online".format(ip))
