#!/usr/bin/env python3
# Script that scans files using VirusTotal API
# https://developers.virustotal.com/reference
# By Ed Goad
# date: 2/5

# Import Python modules
import requests
import hashlib
import configparser
import time
import os
import sys

def get_api_key(key_name):
    # Get the location of the secrets file
    home_dir = os.path.expanduser( "~" )
    secrets_file = os.path.join(home_dir, "secrets.ini" )
    # Create the ConfigParser and load the file
    config = configparser.ConfigParser()
    config.read(secrets_file)
    # Get the API key and return
    api_key = config["APIKeys"][key_name]
    return api_key

def virustotal_get_file_report(token, hash):
    # Setup the  URL
    url = api_base + "/files/" + hash
    # Configure API key 
    headers = { 
        'x-apikey': token,
        'accept': 'application/json'
        }
    payload = {}
    # Perform the request
    response = requests.get(
        url, 
        headers = headers,
        data = payload
        )
    # Convert the JSON to Python objects
    if response.status_code == 200:
        items = response.json()
        return items

def virustotal_get_analysis(token, id):
    # Setup the  URL 
    url = api_base + "/analyses/" + id
    # Configure API key 
    headers = {
        'x-apikey': token,
        'accept': 'application/json'
        }
    payload = {}
    # Perform the request
    response = requests.get(
        url, 
        headers = headers,
        data = payload
        )
    # Convert the JSON to Python objects
    if response.status_code == 200:
        items = response.json()
        return items

def virustotal_upload_file(token, file_path):
    # Setup the base URL and Authorization header
    url = api_base + "/files"
    # Configure API key
    headers = { 
        'x-apikey': token,
        'accept': 'application/json'
        }
    
    # Separate file_name from file_path
    file_name = os.path.basename(file_path)
    # Setup file for upload
    files = {
        'file': (
            file_name,
            open(file_path, 'rb')
            ) 
        }
    
    # Perform the request
    response = requests.post(
        url, 
        files=files,
        headers = headers
        )
        # Convert the JSON to Python objects
    if response.status_code == 200:
        items = response.json()
        return items

def hash_file(file_path):
    # Setup buffer size and sha1 variables
    buff_size = 65535
    sha256 = hashlib.sha256()
    # Open the file for reading in binary
    with open(file_path, 'rb') as f:
        while True:
            # Read a chunk of data
            data = f.read(buff_size)
            # If we reached the end, quit while loop
            if not data:
                break
            # Update sha256 hash with data chunk
            sha256.update(data)
    # Return sha-256 hash
    return sha256.hexdigest()

# Get API key from file
token = get_api_key( "VirusTotal" )
api_base = "https://www.virustotal.com/api/v3"

# Prompt user for file to check
target_file = input( "What file do you wish to scan? " )

# Generate SHA hash
print( "Generating file hash: ", end="" )
file_hash = hash_file(target_file)
print(file_hash)

# Check /file/report using SHA
print( "Getting file report." )
vt_file_report = virustotal_get_file_report(token, file_hash)

# Check if a scan has already been performed
if vt_file_report:
    print( "File report found: " )
    # get analysis stats
    vt_analysis_stats = vt_file_report["data"]["attributes"]["last_analysis_stats"]
    # malicious, suspicious, undetected
    print( f"\tMalicious : {vt_analysis_stats['malicious']}" )
    print( f"\tSuspicious: {vt_analysis_stats['suspicious']}" )
    print( f"\tUndetected: {vt_analysis_stats['undetected']}" )
    
    # Quit script
    sys.exit()
else:
    print( "No file report found, uploading for analysis." )
    # Call file upload with file name
    upload_status = virustotal_upload_file(token, target_file)
    analysis_id = upload_status["data"]["id"]
    print( f"\tAnalysis ID: {analysis_id}" )

    # Loop 3 times
    for i in range(3):
        # Wait 30 seconds
        print( "... sleeping for 30 seconds ..." )
        time.sleep(30)
        # Call analysis report
        print( "Getting analysis report." )
        analysis_results = virustotal_get_analysis(token, analysis_id)
        # Check analysis results
        if analysis_results["data"]["attributes"]["status"] == "completed":
            print( "Analysis complete: " )
            # get analysis stats
            vt_analysis_stats = analysis_results["data"]["attributes"]["stats"]
            # malicious, suspicious, undetected
            print( f"\tMalicious : {vt_analysis_stats['malicious']}" )
            print( f"\tSuspicious: {vt_analysis_stats['suspicious']}" )
            print( f"\tUndetected: {vt_analysis_stats['undetected']}" )
            
            # Quit script
            sys.exit()

# attempt counter has expired, print "Try again later"
print( "Scans not finished, try again in a few minutes." )