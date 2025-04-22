#!/user/bin/.vnv/ python3
# Third example of pinging from Python
# By Quentin Athula
# 4/22/2025

# import necessary python modules
import platform
import os

# Define a function to ping an IP address
ip_prefix = "192.168.1."
# determine the current operating system
current_os = platform.system(). lower()
# Loop from 0 - 254
for final_octet in range(254):
    # Assign IP to ping to a variable
    # Adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + str(final_octet + 1)
    if current_os == "windows":
        # Build our ping command for windows
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        # Build our ping command for other operating systems
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    # Execute command and capture exit code
    exit_code = os.system(ping_cmd)
    # print results to console only if successful
    if exit_code == 0:
        print("{0} is online" .format(ip))
