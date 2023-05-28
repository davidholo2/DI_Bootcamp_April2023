def sum_x_x_x_x(x):
    # convert x to string
    x_str = str(x)

    # initialize the sum to 0
    total = 0

    # loop from 1 to 4 and add the appropriate number of x's to the sum
    for i in range(1, 5):
        x_i = int(x_str * i)
        total += x_i

    return total


x = 3
result = sum_x_x_x_x(x)
print(result)
