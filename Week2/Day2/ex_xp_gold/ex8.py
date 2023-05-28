# Ask the user to input a sequence of comma-separated numbers
numbers_str = input("Enter a sequence of comma-separated numbers: ")

# Split the string into a list of numbers using the comma as a separator
numbers_list = numbers_str.split(",")

# Convert the list of strings to a list of integers
numbers_list = [int(num) for num in numbers_list]

# Create a tuple from the list of numbers
numbers_tuple = tuple(numbers_list)

# Print the list and tuple
print(numbers_list)
print(numbers_tuple)
