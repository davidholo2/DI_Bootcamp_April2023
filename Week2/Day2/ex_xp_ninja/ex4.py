from collections import Counter

# get input from user
sentence = input("Enter a sentence: ")

# split sentence into words and count their frequency
word_counts = Counter(sentence.split())

# print frequency of each word
for word, count in word_counts.items():
    print(f"{word}:{count}")
