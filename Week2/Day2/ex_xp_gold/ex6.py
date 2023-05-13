# Ask the user for 7 words and store them in a list named words
words = []
for i in range(7):
    words.append(input("Enter word #" + str(i+1) + ": "))

# Ask the user for a single character and store it in a variable called letter
letter = input("Enter a single character: ")

# Loop through the words list and print the index of the first appearance of the letter variable in each word of the list
for word in words:
    if letter in word:
        print("The index of the first appearance of", letter, "in", word, "is", word.index(letter))
    else:
        print("The letter", letter, "does not appear in the word", word)
