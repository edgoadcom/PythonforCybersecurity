#!/usr/bin/env python3
# Script that connects to HuggingFace and performs a query
# Requires an API key to run - https://huggingface.co/settings/tokens
# By Ed Goad
# date: 1/3

# Import Python modules
import requests
import configparser
import os

def get_api_key(key_name):
    # Get the location of the secrets file
    home_dir = os.path.expanduser("~")
    secrets_file = os.path.join(home_dir, "secrets.ini")
    # Create the ConfigParser and load the file
    config = configparser.ConfigParser()
    config.read(secrets_file)
    # Get the API key and return
    api_key = config["APIKeys"][key_name]
    return api_key

def generate_image(prompt, api_key):
    # Build URI to API
    base_uri = "https://api-inference.huggingface.co/models/"
    model = "black-forest-labs/FLUX.1-dev"
    request_uri = base_uri + model
    request_headers = {
        'Authorization': 'Bearer '+ api_key,
        'Content-Type': 'application/json',
        }
    payload = {
        "inputs": prompt
    }
    r = requests.post(
        request_uri, 
        headers = request_headers, 
        json = payload
        )

    if r.status_code == 200:
        return r.content

# Ask the user for a prompt
prompt = input("Enter a prompt for the image generation (e.g., 'a cat on a beach'): ")

# Get API key
api_key = get_api_key("huggingface")

# Generate the image from text
image_bytes = generate_image(prompt, api_key)

# Save image to file
with open('downloaded_image.jpg', 'wb') as f:
            f.write(image_bytes)