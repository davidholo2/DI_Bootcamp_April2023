def encrypt(text, shift):
    cypher_text = ''
    for letter in text:
        if letter.isalpha():
            # Shift the letter by the given amount
            new_letter_code = ord(letter) + shift
            # If we shifted past 'z' or 'Z', wrap back to 'a' or 'A'
            if letter.islower() and new_letter_code > ord('z'):
                new_letter_code -= 26
            elif letter.isupper() and new_letter_code > ord('Z'):
                new_letter_code -= 26
            cypher_text += chr(new_letter_code)
        else:
            cypher_text += letter
    return cypher_text

def decrypt(cypher_text, shift):
    plain_text = ''
    for letter in cypher_text:
        if letter.isalpha():
            # Shift the letter backwards by the given amount
            new_letter_code = ord(letter) - shift
            # If we shifted past 'a' or 'A', wrap back to 'z' or 'Z'
            if letter.islower() and new_letter_code < ord('a'):
                new_letter_code += 26
            elif letter.isupper() and new_letter_code < ord('A'):
                new_letter_code += 26
            plain_text += chr(new_letter_code)
        else:
            plain_text += letter
    return plain_text

# Get user input
message = input("Enter a message: ")
shift = int(input("Enter a shift amount: "))

# Ask user if they want to encrypt or decrypt
while True:
    action = input("Do you want to encrypt or decrypt? ")
    if action.lower() == "encrypt":
        print("Encrypted message: ", encrypt(message, shift))
        break
    elif action.lower() == "decrypt":
        print("Decrypted message: ", decrypt(message, shift))
        break
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")
