import json

# Sample JSON data
data = {"name": "John Doe", "age": 30, "city": "New York"}

# Convert Python dictionary to JSON string
i_created_string_from_python_dictionary = json.dumps(data)
print(i_created_string_from_python_dictionary)

# Convert JSON string to Python dictionary
i_created_dictionary_from_json = json.loads(i_created_string_from_python_dictionary)
print(i_created_dictionary_from_json)

with open("data.json", "w") as file:
    json.dump(
        data, file
    )  # here we created a file called data.json and dumped the data dictionary into it
    # thing to note is that dump is used to write data into a file and load is used to read data from a file
    # while dumps and loads are used to convert data between python dictionary and json string
# JSON File -> Dictionary
with open(
    "data.json", "r"
) as file:  # here we are opening the data.json file in read mode and loading the data from it into a python dictionary
    loaded_data = json.load(file)

print(loaded_data)
