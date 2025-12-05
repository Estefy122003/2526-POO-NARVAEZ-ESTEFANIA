# Example of Encapsulation in Object-Oriented Programming
# Code written by Estefania Narváez

class BankAccount:
    def __init__(self, owner, balance):
        # Public attribute
        self.owner = owner

        # Private attribute: cannot be accessed directly
        self.__balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.__balance += amount

    # Method to withdraw money safely
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # Getter method to access the private balance
    def get_balance(self):
        return self.__balance

# Creating an object of BankAccount
account = BankAccount("Estefania", 100)

# Performing operations
account.deposit(50)
account.withdraw(30)

# Displaying the final balance
print("Current balance:", account.get_balance())
