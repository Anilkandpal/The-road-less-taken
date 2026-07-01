import re

data = "The rain in Spain"
result = re.search("Spain", data)
print(result)

animals = "The cat in the hat, and a cat in the bag"
animal_result = re.findall("cat")
print(animal_result)
