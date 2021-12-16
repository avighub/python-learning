class SpecialClass():
    '''
    Constructor , gets called when an object of class is created
    self is passed automatically when object is created
    '''

    def __init__(self, arg1):
        print("I am init: " + arg1)
        self.msg = arg1
        print("Message: " + self.msg)

    def somefunction(self):
        print("I am some function")
        print("Using Class variable: "+ self.msg)


# Creating object of class
ob = SpecialClass("Hello")  # Error:  Init will be called automatically and it needs arg1
ob.somefunction()
