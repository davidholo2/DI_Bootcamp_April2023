# Define the dictionary with the birthdays
birthdays = {
    "Alice": "2000/01/01",
    "Bob": "2001/02/02",
    "Charlie": "2002/03/03",
    "Dave": "2003/04/04",
    "Eve": "2004/05/05"
}

# Print a welcome message for the user
print("Welcome to the birthday dictionary.")

# Print all the names in the dictionary
print("The people in the list are:")
for name in birthdays:
    print(name)

# Ask the user to provide a name
name = input("Who's birthday do you want to look up? ")

# Check if the name is in the dictionary
if name in birthdays:
    # If the name is in the dictionary, get the birthday and print it
    birthday = birthdays[name]
    print("{}'s birthday is {}.".format(name, birthday))
else:
    # If the name is not in the dictionary, print an error message
    print("Sorry, we don't have the birthday information for {}.".format(name))
