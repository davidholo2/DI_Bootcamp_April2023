birthdays = {
    'Alice': '1990/01/01',
    'Bob': '1985/02/15',
    'Charlie': '1995/03/25',
    'Dave': '1998/04/12',
    'Eve': '1992/05/23'
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

while True:
    name = input("Who's birthday do you want to look up? ")
    if name in birthdays:
        print("{}'s birthday is {}.".format(name, birthdays[name]))
    else:
        print("Sorry, we don't have the birthday information for {}.".format(name))
        add_new = input(
            "Do you want to add a new birthday for {}? (y/n) ".format(name))
        if add_new == "y":
            new_birthday = input("Enter the birthday (YYYY/MM/DD): ")
            birthdays[name] = new_birthday
            print("Birthday added!")
        else:
            print("OK, maybe next time!")
