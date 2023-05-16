import random


def guess(num):
    random_num = random.randint(1, 5)
    return (num == random_num)


print(guess(4))
