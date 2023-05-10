def even_odd(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append("even")
        else:
            result.append("odd")
    return result

numbers = [1, 2, 3, 4, 5]
print(even_odd(numbers))
