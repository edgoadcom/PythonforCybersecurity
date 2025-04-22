#!/user/bin/.venv/ python3
# A second example of pinging from python
# Created by Quentin athula
# 4/22/2025

# import necessary python modules
import platform
import os

# Assign IP address to ping to a variable
ip = "127.0.0.1"
# Determine the current operating system
current_os = platform.system() . lower()
if current_os == "windows":
    # Build our ping command for windows
    ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
else:
    # Build our ping command for other operating systems
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

# Execute command and capture exit code
exit_code = os.system(ping_cmd)
# print the result to the console
print(exit_code)