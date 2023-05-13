import re

paragraph = """The quick brown fox jumps over the lazy dog. This sentence contains ten words. This is another sentence. It also contains ten words. 
The quick brown fox jumps over the lazy dog. This is the last sentence. It contains ten words too."""

# Count characters
char_count = len(paragraph)
print("Character count:", char_count)

# Count sentences
sentence_count = len(re.findall(r'\w[.?!](\s|$)', paragraph))
print("Sentence count:", sentence_count)

# Count words
word_count = len(paragraph.split())
print("Word count:", word_count)

# Count unique words
unique_words = set(paragraph.split())
unique_word_count = len(unique_words)
print("Unique word count:", unique_word_count)

# Count non-whitespace characters
non_whitespace_count = len(re.findall(r'\S', paragraph))
print("Non-whitespace character count:", non_whitespace_count)

# Average words per sentence
words_per_sentence = word_count / sentence_count
print("Average words per sentence:", round(words_per_sentence, 2))

# Count non-unique words
non_unique_count = word_count - unique_word_count
print("Non-unique word count:", non_unique_count)
