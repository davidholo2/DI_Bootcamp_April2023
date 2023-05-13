import random

games_won = 0
games_lost = 0
play_again = True

while play_again:
    # Get user input
    user_input = input("Guess a number between 1 and 9 (inclusive) or type 'q' to quit: ")

    # Check if user wants to quit
    if user_input.lower() == 'q':
        play_again = False
        continue

    # Convert user input to integer
    try:
        user_num = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9 or type 'q' to quit.")
        continue

    # Get random number
    rand_num = random.randint(1, 9)

    # Check if user guessed correctly
    if user_num == rand_num:
        print("Winner!")
        games_won += 1
    else:
        print("Better luck next time!")
        games_lost += 1

print(f"You won {games_won} games and lost {games_lost} games.")
