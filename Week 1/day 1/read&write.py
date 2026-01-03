with open("sample.txt", "w") as f:
    f.write("Hello everyone!")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)