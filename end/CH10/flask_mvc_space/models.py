import requests

def get_people_in_space():
    """Fetches the current number of people in space from an API."""
    request_uri = "http://api.open-notify.org/astros.json"
    response = requests.get(request_uri)
    
    if response.status_code == 200:
        return response.json().get("number", "Unknown")
    else:
        return "Error fetching data"
