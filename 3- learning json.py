import json

# Sample JSON data
data = {"name": "John Doe", "age": 30, "city": "New York"}

# Convert Python dictionary to JSON string
i_created_string_from_python_dictionary = json.dumps(data)
print(i_created_string_from_python_dictionary)

# Convert JSON string to Python dictionary
i_created_dictionary_from_json = json.loads(i_created_string_from_python_dictionary)
print(i_created_dictionary_from_json)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)
