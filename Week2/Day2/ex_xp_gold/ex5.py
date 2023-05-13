# Create a string of all the letters in the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Loop over each letter in the alphabet
for letter in alphabet:
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(letter, 'is a vowel')
    else:
        print(letter, 'is a consonant')
