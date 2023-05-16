# ex1
def print_builtin_function_results():
    """
    This program demonstrates the usage of Python built-in functions: abs(), int(), input().

    The `abs()` function returns the absolute value of a number. It takes a single argument and returns the absolute value as a positive number.

    The `int()` function converts a given value into an integer. It can convert numeric strings, floating-point numbers, or other numeric types into integers. If no argument is provided, it returns 0.

    The `input()` function is used to take input from the user. It displays a prompt (optional) and waits for the user to enter some value, which is returned as a string.
    """

    # abs()
    num = -10
    abs_result = abs(num)
    print(f"The absolute value of {num} is: {abs_result}")

    # int()
    num_str = "42"
    int_result = int(num_str)
    print(f"The integer value of '{num_str}' is: {int_result}")

    # input()
    user_input = input("Enter your name: ")
    print(f"Hello, {user_input}!")


# Calling the function to print the results
print_builtin_function_results()


# ex2
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # Output: '5 dollars'
print(int(c1))  # Output: 5
print(repr(c1))  # Output: '5 dollars'

result1 = c1 + 5
print(int(result1))  # Output: 10

result2 = c1 + c2
print(int(result2))  # Output: 15

print(c1)  # Output: '5 dollars'

c1 += 5
print(c1)  # Output: '10 dollars'

c1 += c2
print(c1)  # Output: '20 dollars'

try:
    result3 = c1 + c3
except TypeError as e:
    print(e)
