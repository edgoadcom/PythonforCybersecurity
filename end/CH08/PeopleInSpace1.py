import requests

url = "http://api.open-notify.org/astros.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
