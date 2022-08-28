import requests

endpoint = "http://localhost:8000/api/event_providers/"

data = {
    "name": "gong",
    "email": "gong@example.com"
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())