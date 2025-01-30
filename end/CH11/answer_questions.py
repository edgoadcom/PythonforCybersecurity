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

def get_ai_response(prompt, api_key):
    # Build the URI to the API
    base_uri = "https://api-inference.huggingface.co/models/"
    model = "mistralai/Mistral-Nemo-Instruct-2407"
    request_uri = base_uri + model + "/v1/chat/completions"
    
    request_headers = {
        'Authorization': 'Bearer '+ api_key,
        'Content-Type': 'application/json',
        }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    r = requests.post(
        request_uri, 
        headers = request_headers, 
        json = payload
        )

    if r.status_code == 200:
        result = r.json()
        return result
        
# Define assumptions to go along with the questions
assumptions = [
    "I am a teacher.",
    "This is for an elementary school.",
    "Responses should be simple and easy to understand."
]

# Get API key
api_key = get_api_key("huggingface")

# Ask the user for a prompt
question = input("Enter your question: ")

# Join the assumptions and question, and send to API
prompt = "\n".join(assumptions) + f"\n\nQuestion: {question}\nAnswer:"
responses = get_ai_response(prompt, api_key)

# Print responses
for response in responses["choices"]:
    print(response["message"]["content"])