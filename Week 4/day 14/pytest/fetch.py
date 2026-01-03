import requests

def get_user_detail(username):
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print("User name:", user_data["name"])
        print("Public Repositories:", user_data["public_repos"])
    else:
        print("Failed to retrieve data:")
        
get_user_detail("Abhishek25suman")