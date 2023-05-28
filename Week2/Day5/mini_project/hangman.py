import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_length = len(word)
print("The word has", word_length, "letters")

# creating the list to store correct guesses
word_completion = ["*" for _ in range(word_length)]

# creating a list to store incorrect guesses
incorrect_guesses = []

# creating a variable to store the number of body parts added
body_parts = 0

while True:
    # print the current state of the game
    print("Current guess: ", "".join(word_completion))
    print("Incorrect guesses: ", incorrect_guesses)

    # check if the player has lost
    if body_parts == 6:
        print("You lost! The word was:", word)
        break

    # check if the player has won
    if "*" not in word_completion:
        print("Congratulations! You guessed the word:", "".join(word_completion))
        break

    # get player's guess
    guess = input("Guess a letter: ").lower()

    # check if the guess is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid guess. Please enter a single letter.")
        continue

    # check if the player has already guessed the letter
    if guess in word_completion or guess in incorrect_guesses:
        print("You have already guessed that letter.")
        continue

    # check if the guess is in the word
    if guess in word:
        # update the word completion list
        for i in range(word_length):
            if word[i] == guess:
                word_completion[i] = guess
    else:
        # add a body part to the gallows
        body_parts += 1
        incorrect_guesses.append(guess)

        if body_parts == 1:
            print("  O  ")
        elif body_parts == 2:
            print("  O  ")

            print("  |  ")
        elif body_parts == 3:
            print("  O  ")
            print(" /|  ")
        elif body_parts == 4:
            print("  O  ")
            print(" /|\\ ")
        elif body_parts == 5:
            print("  O  ")
            print(" /|\\ ")
            print(" /   ")
        elif body_parts == 6:
            print("  O  ")
            print(" /|\\ ")
            print(" / \\ ")
