"""
Can contain any datatypes
Can contain other colletions like lists , dictionaries , tuples
mutable - added/removed,updated
maintain order (can use index to find)
"""

# list
fruits = ["Orange", "Apple", "Pears", "Banana"]
# Check Data Type
print(type(fruits))
# Print
print(fruits)
# List Slicing
print("List Slicing 3:")
print(fruits[3:])
print("List Slicing 0-3:")
print(fruits[0:3])
print(fruits[0:]) # O till end
print(fruits[:]) # all
print(fruits[:2]) # first 2


# add another item
fruits.append("Guava")
print(fruits)

# add another list
allMixDataTypes = ["String", 2]
fruits.extend(allMixDataTypes)
print(fruits)

# Remove an String item
fruits.remove("Banana")
print(fruits)

# Remove an item by index
fruits.pop(2)
print(fruits)

# Remove last item
fruits.pop(-1)
print(fruits)

# sort similar datatype list
fruits.sort()
print(fruits)

# check for true / false
print("Banana" in fruits)
print("Orange" in fruits)

fruits.append("Guava")
print(fruits)
print(fruits.count("Guava"))
