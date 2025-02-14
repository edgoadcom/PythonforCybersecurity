#!/usr/bin/env python3
# Script that checks URLs against Google's Safe Browsing API
# https://developers.google.com/safe-browsing/v4
# By Ed Goad
# date: 2/5

# Import Python modules
import requests
import configparser
import os

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
platform = input("What platform are you scanning from [LINUX] ") or "LINUX"

# Default threatTypes to "MALWARE"
threat = input("What threat type [MALWARE] ") or "MALWARE"

# Prompt user for threatEntries
url = input("What URL to scan? ") or "http://testsafebrowsing.appspot.com/s/malware.html"

scan_results = check_safebrowsing_url(token, threat, platform, url)
if "matches" in scan_results:
    print("Threats found")
    matches = scan_results["matches"]
    for match in matches:
        print("\t" +
              match["platformType"] + 
              " / " + match["threatType"] + 
              ": " + match["threat"]["url"]
              )
else:
    print("No issues found")