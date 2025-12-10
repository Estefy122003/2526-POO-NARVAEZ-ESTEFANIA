# --------------------------------------------------------
# Weekly Weather Average Program
# Traditional Programming Approach
# Author: Estefanía Narváez
# --------------------------------------------------------

# Function to enter the temperatures for the 7 days
def enter_temperatures():
    temperatures = []
    print("Enter the temperatures for the week:")
    for day in range(1, 8):
        temp = float(input(f"Temperature for day {day}: "))
        temperatures.append(temp)
    return temperatures

# Function to calculate the weekly average
def calculate_average(values):
    return sum(values) / len(values)

# Main function
def main():
    temps = enter_temperatures()
    avg = calculate_average(temps)
    print(f"\nThe weekly temperature average is: {round(avg, 2)} °C")

# Program execution
if __name__ == "__main__":
    main()

