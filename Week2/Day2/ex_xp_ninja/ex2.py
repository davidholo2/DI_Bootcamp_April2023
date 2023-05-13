import random

# 12. Bonus - Ask the user for 10 numbers between -100 and 100
numbers = []
for i in range(10):
    num = int(input(f"Enter a number between -100 and 100 ({i+1}/10): "))
    while num < -100 or num > 100:
        num = int(input(f"Invalid number! Enter a number between -100 and 100 ({i+1}/10): "))
    numbers.append(num)

# Alternatively, 13. Bonus - Generate 10 random numbers between -100 and 100
# numbers = [random.randint(-100, 100) for i in range(10)]

# Alternatively, 14. Bonus - Generate a random number between 50 and 100
# num_of_numbers = random.randint(50, 100)
# numbers = [random.randint(-100, 100) for i in range(num_of_numbers)]

# a. Print the list of numbers in a single line
print("List of numbers:", numbers)

# b. Print the list of numbers sorted in descending order
print("Sorted list of numbers (descending order):", sorted(numbers, reverse=True))

# c. Print the sum of all the numbers
print("Sum of all the numbers:", sum(numbers))

# d. Print a list containing the first and last numbers
print("List of first and last numbers:", [numbers[0], numbers[-1]])

# e. Print a list of all the numbers greater than 50
print("List of numbers greater than 50:", [num for num in numbers if num > 50])

# f. Print a list of all the numbers smaller than 10
print("List of numbers smaller than 10:", [num for num in numbers if num < 10])

# g. Print a list of all the numbers squared
print("List of numbers squared:", [num**2 for num in numbers])

# h. Print the numbers without any duplicates
no_duplicates = list(set(numbers))
print("List of numbers without duplicates:", no_duplicates)
print("Number of unique numbers:", len(no_duplicates))

# i. Print the average of all the numbers
average = sum(numbers) / len(numbers)
print("Average of all the numbers:", average)

# j. Print the largest number
print("Largest number:", max(numbers))

# k. Print the smallest number
print("Smallest number:", min(numbers))

# l. Bonus - Find sum, average, largest and smallest number without using built-in functions
sum_of_numbers = 0
largest_num = float('-inf')
smallest_num = float('inf')
for num in numbers:
    sum_of_numbers += num
    if num > largest_num:
        largest_num = num
    if num < smallest_num:
        smallest_num = num
average_of_numbers = sum_of_numbers / len(numbers)

print("Sum of all the numbers (without built-in functions):", sum_of_numbers)
print("Average of all the numbers (without built-in functions):", average_of_numbers)
print("Largest number (without built-in functions):", largest_num)
print("Smallest number (without built-in functions):", smallest_num)


