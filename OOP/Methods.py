'''
    instance , class , static
'''


class Student():
    # class/static variable
    school = "Telusko"

    # Constructor
    def __init__(self, m1, m2, m3):
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3

    # Instance method - as it works with instance object
    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    # Accessors / Getters
    def get_mark1(self):
        return self.mark1

    # mutators / setters
    def set_mark1(self, value):
        self.mark1 = value

    @classmethod
    def someClassMethod(cls):
        print("This is class method, without self but cls")

    @staticmethod
    def someStaticMethod():
        print("Static method without self and cls")


# Create object/instance

s1 = Student(10, 30, 50)
s2 = Student(3, 7, 9)

print(f'S1 AVG: {s1.avg()}')
print(f'S2 AVG: {s2.avg()}')

s1.set_mark1(32)
print(f'S1 AVG: {s1.avg()}')  # AVG is changed

# calling class method with class name
Student.someClassMethod()

# calling static method
Student.someStaticMethod()
