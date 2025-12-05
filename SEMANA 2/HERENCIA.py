# Example of Inheritance in Object-Oriented Programming
# Code written by Estefania Narváez

# Parent class (superclass)
class Animal:
    def __init__(self, name):
        # Attribute common to all animals
        self.name = name

    # Generic method that will be overridden
    def sound(self):
        return "This animal makes a sound."

# Child class that inherits from Animal
class Dog(Animal):

    # Overriding the sound method
    def sound(self):
        return "The dog barks: Woof woof!"

# Another child class
class Cat(Animal):

    # Overriding the sound method
    def sound(self):
        return "The cat meows: Meow!"

# Creating objects from child classes
dog = Dog("Buddy")
cat = Cat("Snow")

# Displaying sounds
print(dog.name, "-", dog.sound())
print(cat.name, "-", cat.sound())
