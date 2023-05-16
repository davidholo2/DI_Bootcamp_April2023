import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choices(letters, k=length))
    return random_string


random_string = generate_random_string(5)
print(random_string)
