from googletrans import Translator


def translate_words(words):
    translator = Translator()
    translations = {}

    for word in words:
        translation = translator.translate(word, dest='en')
        translations[word] = translation.text

    return translations


french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translations = translate_words(french_words)

print(translations)
