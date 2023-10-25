

# Write a program to append an existing json object and display it ?

import json
existing_json_object = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
new_data = {
    "job": "Engineer",
    "salary": 50000
}
existing_json_object.update(new_data)
updated_json_object = json.dumps(existing_json_object, indent=4)
print(updated_json_object)
