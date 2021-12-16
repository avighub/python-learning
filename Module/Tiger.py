# import Animal
from Animal import attack


def carnivorous():
    print("Tiger is Carnivorous")
    # Animal.attack()  # If Module is imported as import <module>
    attack()  # If function is imported from module


carnivorous()
