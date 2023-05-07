longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the character 'A'. For exit, type 'exit': ")
    if sentence.lower() == "exit":
        break
    if "a" in sentence.lower():
        print("You typed the letter 'a'. You have failed.")
        continue
    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You have set a new longest sentence.")
        
print(f"The longest sentence you have entered is:\n{longest_sentence}")
