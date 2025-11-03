
import json

# Open and read the JSON file
with open("customers.json", "r") as file:
    data = json.load(file)   # data will be a list of dicts
    customer=  {"name":"shree", "age":15, "city":"Delhi"} 
    data.append(customer)

with open("customers.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 makes it look pretty
