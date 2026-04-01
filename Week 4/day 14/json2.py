import json

a = {"name": "Abhishek", "age": 22}

# Convert Python dictionary to JSON and write to file
with open("data.json", "w") as file:
    json.dump(a, file, indent=2)

# Read JSON data from file and print it
with open("data.json", "r") as file:
    data = json.load(file)
    print(json.dumps(data, indent=2))
