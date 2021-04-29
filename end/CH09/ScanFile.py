#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By Ed Goad
# date: 2/5/2021

# Import Python modules
import requests
import json
import hashlib
import configparser
import time
import os

def get_api_key(key_name):
    # Create the ConfigParser and load the file
    config = configparser.ConfigParser()
    config.read("/home/pi/secrets.ini")
    # Get the API key and return
    api_key = config["APIKeys"][key_name]
    return api_key

def check_virustotal_hash(token, hash):
    # Setup the base URL and Authorization header
    url = api_base + "/file/report"
    # Configure API key and file hash
    params = { 'apikey': token,
                'resource': hash
            }
    # Perform the request
    response = requests.get(
        url, 
        params=params
        )
    # Convert the JSON to Python objects
    items = response.json()
    return items

def upload_virustotal_file(token, file_path):
    # Separate file_name from file_path
    file_name = os.path.basename(file_path)
    # Setup the base URL and Authorization header
    url = api_base + "/file/scan"
    # Configure API key
    params = { 'apikey': token }
    # Setup file for upload
    files = { 'file': (file_name, open(file_path, 'rb')) }
    # Perform the request
    response = requests.post(
        url, 
        files=files,
        params=params
        )
    # Convert the JSON to Python objects
    items = response.json()
    return items

def get_virustotal_comments(hash):
    # here
    return True

def hash_file(file_path):
    # Setup buffer size and sha1 variables
    buff_size = 65535
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha1 = hashlib.sha1()
    # Open the file for reading in binary
    with open(file_path, 'rb') as f:
        while True:
            # Read a chunk of data
            data = f.read(buff_size)
            # If we reached the end, quit while loop
            if not data:
                break
            # Update sha1 hash with data chunk
            md5.update(data)
            sha256.update(data)
            sha1.update(data)
    # Return hash
    #print("MD5   : {0}".format(md5.hexdigest()))
    #print("SHA256: {0}".format(sha256.hexdigest()))
    #print("SHA1  : {0}".format(sha1.hexdigest()))
    
    return sha256.hexdigest()


# Get API key from file
token = get_api_key("VirusTotal")
api_base = "https://www.virustotal.com/vtapi/v2"

# Prompt user for file to check
target_file = input("What file do you wish to scan? ")

# Generate SHA hash
file_hash = hash_file(target_file)

# Check /file/report using SHA
file_check = check_virustotal_hash(token, file_hash)

# Check if a scan has already been performed
if file_check['response_code'] == 1:
    print("Scan found")
    print("   {0} scans tested, {1} positive".format( \
        file_check['total'], file_check['positives']))
    print("   More details can be found at: {0}".format( \
        file_check['permalink']))
else:
    print("File not previously scanned, submitting")
    # Upload file to /file/scan
    upload_virustotal_file(token, target_file)
    print("File uploaded, sleeping for a maximum of 2 minutes")
    # Perform max of 6 loops, with a pause
    for i in range(3):
        # Sleep for 21 seconds
        # 21 is needed to due to API limit of 4/minute
        time.sleep(21)
        # Check for completed scan
        file_check = check_virustotal_hash(token, file_hash)
        if file_check['response_code'] == 1:
            # Successful scan found, print results and quit loop
            print("Results returned")
            print("   {0} scans tested, {1} positive".format( \
                file_check['total'], file_check['positives']))
            print("   More details can be found at: {0}".format( \
                file_check['permalink']))
            break

# If no results found, quit and suggest trying later
if file_check['response_code'] != 1:
    print("Scans not finished, try again in a few minutes")

