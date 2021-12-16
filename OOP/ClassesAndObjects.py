"""
supports inheritance (multiple)
supports polymorphism
_init_ method: sets attributes for an object during object creation - Constructor
    - not required by defaul but is used to set default state of object
    - it is the first method for a class
self : self referencing variable
    - used to reference the object that is constructed by init method
"""


class Person:
    def __init__(self, firstname, lastname, city):
        "Doc string: initialize attributes to be used in/available for all \
        class methods in this class and for class , object created by class"

        self.firstname = firstname
        self.lastname = lastname
        self.city = city

    def introduce(self):
        "Everyone introduce themselves"
        print("Hi I am {} {} and I stay in {}".format(self.firstname, self.lastname, self.city))


Avishek = Person("Avishek", "Behera", "Bangalore")
print("Hello I am {} {} and I stay in {}".format(Avishek.firstname, Avishek.lastname, Avishek.city))
Avishek.introduce()


# Inheritance
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, city):
        super().__init__(firstname, lastname, city)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.city = "Hyderabad"
        elif self.weapon == "tree":
            other.city = "Pune"
        else:
            other.city = "BBSR"

    def introduce(self):
        print("I am {} and I am Imortal".format(self.firstname))

# Creating object and Enemy Class
Alex = Enemy('rock', "Avishek", "Behera", "Bangalore")
Alex.hurt(Avishek)
Avishek.introduce()
Alex.introduce()
