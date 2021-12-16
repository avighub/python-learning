"""
Similar to LIST
Can contain different types of DATA TYPEs
Read only and unmutable
separated by Comma and paranthesis
Use tuple if it does not need to be changed , rather List
"""

# list
fruits = ["Orange", "Apple", "Pears", "Banana"]
print(type(fruits))
print(fruits)

# Tuple
fruits2 = ("Orange", "Apple", "Pears", "Banana")
print(type(fruits2))
print(fruits2)
# List Slicing
print("Tuple Slicing 3:")
print(fruits2[3:])
print("Touple Slicing 0-3:")
print(fruits2[0:3])

#adding value to tuple
fruits2[2]="Guava" # Throws Error: TypeError: 'tuple' object does not support item assignment