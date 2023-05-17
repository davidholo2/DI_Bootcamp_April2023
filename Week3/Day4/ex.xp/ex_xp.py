# ex1
import json
import random


def get_words_from_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            line_words = line.split()
            words.extend(line_words)

    return words


def get_random_sentence(length):
    str_list = get_words_from_file('Week3\Day4\ex.xp\sowpods.txt')
    random_elements = random.sample(str_list, length)
    return random_elements


def create_random_sentence(word_list):
    sentence = ' '.join(word_list)
    sentence = sentence.lower()
    return sentence


def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program make a Random sentance in the leangth of the input")
    print("and generates a sentence in lowercase.")
    print("Let's create a random sentence!")


def get_number():
    while True:
        try:
            num = int(input("Enter a number between 2-20: "))
            if not (2 <= num <= 20):
                raise ValueError("Please enter a number between 2-20.")
            return num
        except ValueError as e:
            print(e)


main()
num = get_number()
list_of_words = get_random_sentence(num)
print(create_random_sentence(list_of_words))


# ex2

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)
data["company"]["employee"]["birth_date"] = "1990-01-01"
with open("output.json", "w") as file:
    json.dump(data, file)
print("JSON data saved to 'output.json'.")
