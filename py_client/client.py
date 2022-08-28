import requests
from django.utils import timezone

endpoint = "http://localhost:8000/api/event_providers_rest/"

# get_response = requests.get(endpoint, 
# params={"abc": 123}, # query parameters in the endpoint
# json={"query": "hello world"}
# )

get_response = requests.post(endpoint, json={"name1": "hello world", "email": "test"})

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())