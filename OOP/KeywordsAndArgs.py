"""
******function with arguments******
- Function can have params
    - Can be called by just the name of function
    - Params can be in sequence or arguments
- In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
    1.)*args (Non-Keyword Arguments)
    2.)**kwargs (Keyword Arguments)
"""


# ##### Exercise 1
# def addUserDetails(name, age, city):
#     print("User's Name: {} , age: {} , city: {}".format(name, age, city))
#
#
# # Overloaded method
# def addUserDetails(name, city, age=33):  # default value params must be at the end
#     print("User's Name: {} , age: {} , city: {}".format(name, age, city))
#
#
# addUserDetails("Avishek", 33, "Bangalore")  # With the correct sequence
# addUserDetails("Avishek", "bangalore")  # Takes the default value if arg is not provided
# addUserDetails(age=33, name="Avishek", city="Bangalore")

# ##### Exercise 2 - *args
# def argExercise(*args):
#     print(args)
#
#
# argExercise("Avishek", "behera")
# argExercise(3, 10)
#
#
# def argExercise2(*args):
#     for arg in args:
#         print(arg)  # For each
#
#
# argExercise2("Hello", "I am Avishek")

# ##### Exercise 3 - *kwargs
# def kwArgs1(**kwargs):
#     for key, value in kwargs.items():
#         print("Key is:%s Value is: %s" % (key, value))
#
#
# kwArgs1(name="Avishek", age=33)
#
#
# def kwArgs2(**kwargs):
#     print(kwargs)
#
#
# kwArgs2(name="Avishek", age=33)


# ##### Exercise 4 - args + *args + **kwargs
def mixOfArgs(name, company, *args, **kwargs):
    print("My Name {} and I work at {}, My Salary is {} and Designation is {}".format(name, company, args, kwargs))


mixOfArgs("avishek", "Schneider Electric", 10000, QA="Test Engineer")


# ##### Exercise 5 - using  *args  **kwargs to call function
def userInfo(name, company, salary):
    print(name, company, salary)


args = ("Avishek", "SE", 30000)
userInfo(*args)
