#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
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

def list_respositores(token):
    # Setup the base URL and Authorization header
    url = "https://api.github.com/user/repos"
    headers = { 'Authorization' : "token " + token }
    # Perform the request
    response = requests.get(
        url, 
        headers=headers
        )
    # Convert the JSON to Python objects
    items = response.json()
    return items

# Get API key from file
token = get_api_key("GitHub")

# Get repositories
repositories = list_respositores(token)
# For each repo, print out the name
for repository in repositories:
    print(repository["name"])

