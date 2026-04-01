import requests

response = requests.get("https://api.github.com/invalid-url")

if response.status_code == 200:
    print("Success")               #users
elif response.status_code == 404:
    print("Resource Not Found")    #invalid-url
elif response.status_code == 401:
    print("Unauthorized")          #user
else:
    print("Server Error:", response.status_code)