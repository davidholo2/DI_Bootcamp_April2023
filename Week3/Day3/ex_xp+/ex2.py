import random


def guess(num):
    random_num = random.randint(1, 100)
    return (num == random_num)


print(guess(4))
