import requests
import json

url = "http://api.open-notify.org/astros.json"

# GET request
response = requests.get(url)
print(response.json())

# data to send
post_data = {
    "name": "Abhishek",
    "age": 22
}

# POST request
response = requests.post(url, json=post_data)
print(response.status_code)
