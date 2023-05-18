class AnagramChecker:
    def __init__(self, wordlist_file):
        self.wordlist = self.load_wordlist(wordlist_file)

    def load_wordlist(self, wordlist_file):
        with open(wordlist_file, 'r') as file:
            return file.read().split()

    def is_valid_word(self, word):
        return word.lower() in self.wordlist

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        anagrams = []
        for w in self.wordlist:
            if self.is_anagram(w, word):
                anagrams.append(w)
        return anagrams
