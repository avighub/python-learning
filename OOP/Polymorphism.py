"""
Duck typing

"""

class A:
    def execute(self):
        print("Walking")


class B:
    def execute(self):
        print("Swimming")

class C:
    def feature(self,behavior):
        behavior.execute()

a = A()
b = B()
obj = C()
obj.feature(a)
obj.feature(b)


# =========overloading

