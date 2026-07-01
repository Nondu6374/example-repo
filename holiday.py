# Define the hotel cost function
def hotel_cost(num_nights):
    """
    Calculate the total hotel cost based on the number of nights.

    Args:
    num_nights (int): The number of nights staying at the hotel.

    Returns:
    int: The total cost of the hotel stay (price per night: R1000).
    """
    PRICE_PER_NIGHT = 1000 # Cost per night in rands
    return PRICE_PER_NIGHT * num_nights

# Define the plane cost function
def plane_cost(city_flight):
    """
    Calculate the flight cost based on the destination city.

    Args:
    city_flight (str): The chosen destination city.
    """
    if city_flight.lower() == "cape town": return 1000
    elif city_flight.lower() == "durban": return 1500
    elif city_flight.lower() == "johannesburg": return 1200
    elif city_flight.lower() == "port elizabeth": return 1600
    else:
        print("City not recognized. Defaulting to Johannesburg.")
        return 1200

# Define the car rental cost function
def car_rental(rental_days):
    """
    Calculate the total car rental cost based on the number of rental days.

    Args:
    rental_days (int): The number of days the car is rented.

    Returns:
    int: The total cost of the car rental (price per day: R500).
    """
    PRICE_PER_DAY = 500  # Cost per rental day in rands
    return PRICE_PER_DAY * rental_days

# Define the total holiday cost function
def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculate the total holiday cost by combining hotel, flight, and car rental costs.

    Args:
    num_nights (int): Number of nights staying at the hotel.
    city_flight (str): Destination city for the flight.
    rental_days (int): Number of days the car is rented.

    Returns:
    int: Total holiday cost.
    """
    hotel_total = hotel_cost(num_nights)
    flight_total = plane_cost(city_flight)
    car_total = car_rental (rental_days)
    return hotel_total + flight_total + car_total

# --- Main Program ---
print("Welcome to the Holiday Cost Calculator!")
print("\nWe off flights to the following cities:")
print("1. Cape Town")
print("2. Durban")
print("3. Johannesburg")
print("4. Port Elizabeth")

# Get user inputs
city_flight = input("\nPlease enter the city you are flying to:")
num_nights = int(input("Please enter the number of nights you will be staying ath the hotel:"))
rental_days = int(input("Please enter the number of days you will be renting a car"))

# Calculate the total holiday cost
total_cost = hotel_cost(num_nights)
flight_total = plane_cost(city_flight)
car_total = car_rental(rental_days)

# Pint all holiday details
print("\n" + "=" * 40)
print("Holiday Cost Breakdwon")
print("=" *40)
print(f"Destination City: {city_flight.title()}")
print(f"Number of Nights: {num_nights}")
print(f"Rental Days {Rental_days}")
print("-" * 40)
print(f"Hotel Cost: R{hotel_total}")
print(f"Flight Cost: R{flight_total}")
print(f" Car Rental Cost: R(car_total)")
print("-" * 40)
print(f"TOTAL HOLIDAY COST: R{total_cost}")
print("=" * 40)

# Output with different input combinations to show compatibility
print("\nCompatibility Check:")
print("Example 1 - Cape Town for 3 nights, 2 rental days:")
# This just demonstrates the calculation logic without getting the user input again
test_cost = holiday_cost(3, "Cape Town",2)
print(f" Total cost: R{test_cost}\n")

print("Example 2 - Durban for 5 nights, 4 rental days:")
test_cost = holiday_cost(5, {"Durban", 4})
print(f" Total cost: R{test_cost}\n")

print("Example 3 - Johannesburg for 1 night, 0 rental days:")
test_cost = holiday_cost(1, "Johannesburg", 0)
print(f" Total cost: r{test_cost}\n")









    