import requests

eventprovider_id = input("what is the event provider id you wanna delete?")

try:
    eventprovider_id = int(eventprovider_id)
except:
    eventprovider_id = None
    print(f'{eventprovider_id} is not a valid id')

if eventprovider_id:
    endpoint = f"http://localhost:8000/api/event_providers/{eventprovider_id}/delete/"

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code==204)