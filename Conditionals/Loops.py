"""
for loop can be used to  iterate over a dictionary or list
range can be used to iterate over a specified range excluding last occurance
"""
# for loop
fruits = ["Orange", "Apple", "Pears", "Banana"]
for fruit in fruits:
    print("Would you like to have {} ?".format(fruit))

# for loop - range
for number in range(1, 11):
    print("Number is {}".format(number))

# While Loop
print("================")
temp_f = 40
while temp_f >= 35:
    print("Current temp: {}".format(temp_f))
    temp_f -= 1

# Loop control - Break
print("================")
for number in range(1, 11):
    if number == 3:
        break
    print("Number is {}".format(number))

# Loop control - Continue
# skips current loop from there and continues the further loops
print("================")
for number in range(1, 11):
    if number == 3:
        print("We are skipping 3")
        continue
    print("Number is {}".format(number))

# Loop control - pass
# Does nothing and continues to next loop
print("================")
for number in range(1, 11):
    if number == 3:
        print("We are passing 3")
        pass
    print("Number is {}".format(number))

# fWhile on
# Does nothing and continues to next loop
print("================")
for number in range(1, 11):
    if number == 3:
        print("We are passing 3")
        pass
    print("Number is {}".format(number))
