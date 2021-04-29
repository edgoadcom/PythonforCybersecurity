#!/usr/bin/env python3
# Script that checks URLs against Google's Safe Browsing API
# https://developers.google.com/safe-browsing/v4
# By Ed Goad
# date: 2/5/2021

# Import Python modules
import requests
import json
import configparser

def get_api_key(key_name):
    # Create the ConfigParser and load the file
    config = configparser.ConfigParser()
    config.read("/home/pi/secrets.ini")
    # Get the API key and return
    api_key = config["APIKeys"][key_name]
    return api_key

def check_safebrowsing_url(token, threat, platform, test_url):
    clientId = "test_python_client"
    clientVersion = "0.0.1"
    # Setup the base URL and Authorization header
    api_base = "https://safebrowsing.googleapis.com/v4"
    url = api_base + "/threatMatches:find?key=" + token
    # Configure API key and file hash
    params = { "client": { 
                    "clientId": clientId,
                    "clientVersion": clientVersion
                },
                "threatInfo": {
                    "threatTypes": threat,
                    "platformTypes": platform,
                    "threatEntryTypes": "URL",
                    "threatEntries": {
                        "url": test_url
                    }
                }
            }
    # Perform the request
    response = requests.post(
        url, 
        json=params
        )
    # Convert the JSON to Python objects
    items = response.json()
    return items


# Get API key
token = get_api_key("GoogleSafeBrowsing")

# Prompt user for platformTypes, Default to "LINUX"
platform = input("What platform are you scanning form [LINUX] ") \
    or "LINUX"

# Default threatTypes to "MALWARE"
threat = input("What threat type [MALWARE] ") or "MALWARE"

# Prompt user for threatEntries
url = input("What URL to scan? ") or \
    "http://testsafebrowsing.appspot.com/s/malware.html"

print(check_safebrowsing_url(token, threat, platform, url))