class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_list = self.text.split()
        frequency = word_list.count(word)
        if (frequency == 0):
            return None
        return frequency

    def most_common_word(self):
        word_list = self.text.split()
        word_count = {}
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + 1
        most_common = max(word_count, key=word_count.get)
        return most_common

    def unique_words(self):
        word_list = self.text.split()
        unique_words = list(set(word_list))
        return unique_words

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return cls(text)


my_text = "A good book would sometimes cost as much as a good house."
my_text_analysis = Text(my_text)
frequency = my_text_analysis.word_frequency("good")
print(f"Frequency of 'good': {frequency}")
most_common = my_text_analysis.most_common_word()
print(f"Most common word: {most_common}")
unique_words = my_text_analysis.unique_words()
print("Unique words:", unique_words)

text_instance = Text.from_file('Week3\\Day4\\dc\\the_stranger.txt')
frequency = text_instance.word_frequency("good")
print(f"Frequency of 'good': {frequency}")
most_common = text_instance.most_common_word()
print(f"Most common word: {most_common}")
unique_words = text_instance.unique_words()
print("Unique words:", unique_words)
