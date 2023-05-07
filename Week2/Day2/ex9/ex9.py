total_cost = 0

while True:
    age_str = input("Enter the age of a family member (or 'done' if finished): ")
    if age_str == 'done':
        break
    age = int(age_str)
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_cost += ticket_price

print("The total cost of all tickets is $", total_cost)
######################################################################
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]
allowed_names = []

for name in names:
    age_str = input("Enter the age of {}: ".format(name))
    age = int(age_str)
    if age >= 16 and age <= 21:
        allowed_names.append(name)

print("The following teenagers are allowed to watch the movie:", allowed_names)

