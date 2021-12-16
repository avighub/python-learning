"""
key/value pair
mutable
order of entry
"""

# key value
people = {"name": "Avishek", "city": "Bangalore", "age": 33}
print(people)

# get items
print(people.items())
# get keys
print(people.keys())

# update
people.update(age=35)
print(people)

#remove last item
people.popitem()
print(people)

# update with another dict
new_dict = {"name":"Akankshya","city":"Hyderabad"}
people.update(new_dict)
print(people)