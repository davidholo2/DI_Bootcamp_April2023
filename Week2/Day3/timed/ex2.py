num = int(input("Enter the number: "))

# Find the divisors and sum them up
divisors = [i for i in range(1, num) if num % i == 0]
divisor_sum = sum(divisors)

# Check if the number is a perfect number
if num == divisor_sum:
    print(True)
else:
    print(False)
