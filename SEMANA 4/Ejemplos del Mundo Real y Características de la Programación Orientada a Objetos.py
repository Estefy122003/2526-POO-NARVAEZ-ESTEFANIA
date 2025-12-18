# This class represents a room in a reservation system
class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.available = True

    # Method to reserve the room
    def reserve(self):
        if self.available:
            self.available = False
            return "Room reserved successfully."
        else:
            return "Room is not available."


# This class represents a customer
class Customer:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


# This class represents a reservation
class Reservation:
    def __init__(self, customer, room):
        self.customer = customer
        self.room = room

    # Method to make a reservation
    def make_reservation(self):
        result = self.room.reserve()
        print("Customer:", self.customer.name)
        print("Room number:", self.room.number)
        print(result)


# Main program
def main():
    room1 = Room(101, "Single", 35)
    customer1 = Customer("John Perez", "0102030405")

    reservation1 = Reservation(customer1, room1)
    reservation1.make_reservation()


main()
