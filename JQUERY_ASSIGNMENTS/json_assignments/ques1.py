

# Write a program to manipulate string using dumps() & loads() ?

import json
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print("Serialized JSON String:", json_string)


parsed_data = json.loads(json_string)
print("Deserialized Dictionary:", parsed_data)

parsed_data["age"] = 31
parsed_data["city"] = "San Francisco"
updated_json_string = json.dumps(parsed_data)
print("Updated Serialized JSON String:", updated_json_string)
