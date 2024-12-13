#!/usr/bin/env python3
# Port scanner example 
# Use 'sudo apt -y install python3-pip' to install pip
# Use 'sudo apt -y install nmap' to install nmap
# Use 'pip3 install python-nmap' to install modules
# By Ed Goad
# 12/12

# import necessary Python modules
import nmap

# Identify target address
target_addresses = "192.168.0.0/24"

# Identify the ports for the scan
ports = "1-100"

# Create the scanner object
scanner = nmap.PortScanner()

# Scan the network
results = scanner.scan(target_addresses, ports, arguments="-T5")

# Report results
for target, host in results['scan'].items():
    print(target)

    # If open ports are found, print the current state
    if 'tcp' in host:
        for port, status in host['tcp'].items():
            print(f"\t{port} - {status['state']} ({status['name']})")
