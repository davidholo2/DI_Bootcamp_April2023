# take user input
sentence = input("Enter a sentence: ")

# split the sentence into words
words = sentence.split()

# reverse the order of the words
words = words[::-1]

# join the words into a new sentence
new_sentence = " ".join(words)

# print the new sentence
print(new_sentence)
