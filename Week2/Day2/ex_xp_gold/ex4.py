# Ask the user for three numbers
max_num = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))

# Compare the second and third numbers with the first and update the maximum if necessary
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3

# Print the maximum number
print("The maximum number is:", max_num)
