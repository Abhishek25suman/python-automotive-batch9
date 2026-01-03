import requests

url = "https://api.github.com/users"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.ok:
    for user in response.json():
        print(user)