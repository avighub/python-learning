"""
************* TAU PYTHON Training ***********
Multiline comments for documentations
two types of variables
    class
    instance ( declared in constructor)
"""
# ##################Exercise 1
# _cars = 23
# cars = 24
# CARS = 25
#
# number_of_cars = 23
# kind_of_cars = "Ferrari"
#
# print(_cars)
# print(cars)
# print(CARS)
# print(number_of_cars)
# print(kind_of_cars)

# ################Exercise 2
name = "Avishek"
company = "Schneider Electric"
print(name + company)  # No space
print(name + " " + company)
print("%s works at %s" % (name, company))  # Using variable,Old way
print("{} works at {}".format(name, company))  # Using variable , most used way
print(f'{name} works at {company}') # Modern way
