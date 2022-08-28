import requests
from getpass import getpass

# endpoint = "http://localhost:8000/api/event_providers/"
auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_response = requests.post(auth_endpoint, json={"username": 
username, 'password': password}) # getting the auth token for this user from the database
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/event_providers/"
    get_response = requests.get(endpoint, headers=headers) # pass in the authentication token header
    print(get_response.json())