# define sandwich orders list
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]

# print message for running out of pastrami
print("Sorry, we have run out of pastrami sandwiches.")

# remove all occurrences of pastrami sandwiches using a while loop
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# define finished sandwiches list
finished_sandwiches = []

# simulate making each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print("I'm making a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches are ready!")
print("List of finished sandwiches: ", finished_sandwiches)
