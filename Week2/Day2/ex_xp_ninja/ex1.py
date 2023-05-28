import math

# fixed values of C and H
constants = (50, 30)
C, H = constants

# ask user for comma-separated string of numbers
user_input = input("Enter comma-separated numbers: ")

# split the input into a list of numbers
numbers = user_input.split(",")

# initialize an empty list to store results
results = []

# calculate the result for each number and add it to the results list
for number in numbers:
    D = int(number)
    Q = round(math.sqrt((2 * C * D) / H))
    results.append(str(Q))

# print the results as a comma-separated string
print(",".join(results))
