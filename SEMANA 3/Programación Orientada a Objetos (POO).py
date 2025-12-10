# ----------------------------------------------------------
# Weekly Weather Average Program
# Object-Oriented Programming Approach
# Author: Estefanía Narváez
# ----------------------------------------------------------

# Base class: handles storing temperatures and calculating the average
class WeeklyWeather:
    def __init__(self):
        # Encapsulated attribute (not strictly private but protected by convention)
        self._temperatures = []

    # Method to enter temperatures
    def enter_temperatures(self):
        print("Enter the temperatures for the week (OOP mode):")
        for day in range(1, 8):
            temp = float(input(f"Temperature for day {day}: "))
            self._temperatures.append(temp)

    # Method to calculate the average
    def calculate_average(self):
        if not self._temperatures:
            return 0
        return sum(self._temperatures) / len(self._temperatures)

# Child class (Inheritance)
class ExtendedWeather(WeeklyWeather):

    # Polymorphism: different way to display the result
    def show_average(self):
        average = self.calculate_average()
        print(f"\nThe weekly temperature average is: {round(average, 2)} °C")

# Main program execution
if __name__ == "__main__":
    weather = ExtendedWeather()
    weather.enter_temperatures()
    weather.show_average()
