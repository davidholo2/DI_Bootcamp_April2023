names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask the user for their name
name = input("What is your name? ")

# Check if the name is in the list
if name in names:
    index = names.index(name)
    print("The index of the first occurrence of your name is:", index)
else:
    print("Your name was not found in the list.")
