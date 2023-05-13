# create a list of numbers from one to one million
numbers = list(range(1, 1000001))

# use min() and max() to check that the list starts at one and ends at one million
print("Minimum number in the list:", min(numbers))
print("Maximum number in the list:", max(numbers))

# use sum() to calculate the sum of the numbers in the list
print("Sum of numbers in the list:", sum(numbers))

for number in numbers:
    print(number)