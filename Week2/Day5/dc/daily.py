user_input = input("Enter a comma-separated sequence of words: ")
words = [word.strip() for word in user_input.split(",")]
sorted_words = sorted(words)
result = ", ".join(sorted_words)
print(result)
