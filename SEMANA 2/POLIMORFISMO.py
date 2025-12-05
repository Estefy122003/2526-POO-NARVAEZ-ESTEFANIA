# Example of Polymorphism in Object-Oriented Programming
# Code written by Estefania Narváez

# Parent class
class Bird:
    # General method
    def make_sound(self):
        return "Bird sound"

# Child class that overrides the method
class Parrot(Bird):
    def make_sound(self):
        return "Parrot says: Hello!"

# Another child class
class Eagle(Bird):
    def make_sound(self):
        return "Eagle screams!"

# Function that demonstrates polymorphism
# It works with any object that has the method make_sound()
def animal_sound(animal):
    print(animal.make_sound())

# Creating objects from child classes
parrot = Parrot()
eagle = Eagle()

# Calling the same function with different objects
animal_sound(parrot)
animal_sound(eagle)
