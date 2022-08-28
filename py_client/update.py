import requests

endpoint = "http://localhost:8000/api/event_providers/1/update/"

data = {
    "name": "changed",
    "email": "new@example.com"
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())