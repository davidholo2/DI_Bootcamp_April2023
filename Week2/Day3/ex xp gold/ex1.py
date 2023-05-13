# initialize the birthdays dictionary
birthdays = {
    "John": "1995/02/10",
    "Emily": "1998/04/22",
    "Michael": "1989/07/15",
    "Sarah": "1992/11/27",
    "David": "1987/01/01"
}

# print a welcome message
print("Welcome! You can look up the birthdays of the people in the list!")

# ask the user for a name
name = input("Whose birthday do you want to look up? ")

# get the birthday of the person
birthday = birthdays.get(name)

# print out the birthday with a message
if birthday:
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, we don't have the birthday for {name}.")
