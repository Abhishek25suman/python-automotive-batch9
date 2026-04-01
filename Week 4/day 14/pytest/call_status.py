import requests

session = requests.Session()

response1 = session.get("https://api.github.com/users")
response2 = session.get("https://api.github.com/users")

print("First Call Status:", response1.status_code)
print("Second Call Status:", response2.status_code)