import json

# Open and read the JSON file
with open("customers.json", "r") as file:
    data = json.load(file)
print(data)
