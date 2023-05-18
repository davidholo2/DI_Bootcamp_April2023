from anagram_checker import AnagramChecker


def display_menu():
    print("--- Anagram Checker ---")
    print("1. Input a word")
    print("2. Exit")
    choice = input("Please enter your choice (1/2): ")
    return choice


def validate_word(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False
    elif not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    else:
        return True


def process_word(word):
    word = word.strip()
    checker = AnagramChecker("Week3\Day5\Anagram\sowpods.txt")
    anagrams = checker.get_anagrams(word)

    print(f"\nWord: {word}")
    print("Anagrams:")
    if anagrams:
        for anagram in anagrams:
            print(anagram)
    else:
        print("No anagrams found.")


def main():
    while True:
        choice = display_menu()

        if choice == "1":
            word = input("Please enter a word: ")
            if validate_word(word):
                process_word(word)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("Thank you for using the Anagram Checker!")


main()
