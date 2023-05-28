import random


def throw_dice():
    """
    Simulate rolling of a dice, return an integer between 1 and 6
    """
    return random.randint(1, 6)


def throw_until_doubles():
    """
    Keep throwing 2 dice until they both land on the same number (doubles),
    return the number of throws it took to get doubles
    """
    throws = 0
    while True:
        throws += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice1 == dice2:
            return throws


def main():
    """
    Call throw_until_doubles 100 times and store results in a list.
    Then print total throws and average throws to reach doubles.
    """
    results = []
    for i in range(100):
        throws = throw_until_doubles()
        results.append(throws)

    total_throws = sum(results)
    avg_throws = round(total_throws / 100, 2)
    print("Total throws:", total_throws)
    print("Average throws to reach doubles:", avg_throws)


if __name__ == '__main__':
    main()
