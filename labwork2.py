# Display welcome message and room options
print("Welcome to Bookings.Com")
print("Here are the selection of rooms available:")
print("1. Single - RM 100 per night")
print("2. Double - RM 150 per night")
print("3. Suites - RM 250 per night")

# Define room rates
Single = 100
Double = 150
Suites = 250

# Get user input for room choice, number of rooms, and number of nights
choice = input("Please select your preferred room (Single, Double, or Suites): ")
num_room = int(input("Please enter the number of rooms to be reserved: "))
num_days = int(input("Please enter the number of nights to be reserved: "))

# Calculate total cost based on user input
if choice == "Single":
    total_cost = Single * num_room * num_days
    print("Your total is:RM", total_cost)

    # Apply discount for more than 5 rooms
    if num_room > 5:
        total_cost_disc = total_cost - (total_cost * 0.1)
        print("Congratulations! Your new discounted price is:RM", total_cost_disc)

    # Offer complimentary breakfast for more than 7 nights
    if num_days > 7:
        print("Congratulations! You get a complimentary breakfast voucher.")

elif choice == "Double":
    total_cost = Double * num_room * num_days
    print("Your total is:RM", total_cost)

    # Apply discount for more than 5 rooms
    if num_room > 5:
        total_cost_disc = total_cost - (total_cost * 0.1)
        print("Congratulations! Your new discounted price is:RM", total_cost_disc)

elif choice == "Suites":
    # Check minimum stay requirement for Suites
    if num_days < 3:
        print("Sorry, minimum stay for a Suite is 3 nights.")
    else:
        total_cost = Suites * num_room * num_days
        print("Your total is:RM", total_cost)

        # Apply discount for more than 5 rooms
        if num_room > 5:
            total_cost_disc = total_cost - (total_cost * 0.1)
            print("Congratulations! Your new discounted price is:RM", total_cost_disc)

else:
    print("Wrong input... Please re-enter the correct input.")
