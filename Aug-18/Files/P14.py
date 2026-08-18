import json
with open("c:/files/data.json", "r") as read_file:
    b = json.load(read_file)
print(b)