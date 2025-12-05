# Example of Abstraction in Object-Oriented Programming
# Code written by Estefania Narváez

from abc import ABC, abstractmethod

# Abstract class: cannot be instantiated
class Vehicle(ABC):

    # Abstract method: must be implemented by child classes
    @abstractmethod
    def start_engine(self):
        pass

# Concrete class that inherits from Vehicle
class Car(Vehicle):

    # Implementation of the abstract method
    def start_engine(self):
        return "The car engine is starting..."

# Creating an object of the Car class
car = Car()

# Calling the abstracted functionality
print(car.start_engine())
