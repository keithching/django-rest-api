import requests

endpoint = "http://localhost:8000/api/event_providers/12345/"

get_response = requests.get(endpoint)
print(get_response.json())