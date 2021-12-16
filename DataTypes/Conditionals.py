"""
Condition check occurs from top to bottom
Once the condition is matched others do not matter
"""

name = input("Enter Your name:")
if name == "Avishek":
    print("Hello Avi")
elif name == "Akankshya":
    print("Hello AKN")
else:
    print("Thanks For entering Name.")
print("Have a Great Day.")