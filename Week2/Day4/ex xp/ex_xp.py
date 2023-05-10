#ex1
def display_message():
    print("im learing to become a full stack dev")


display_message()

#ex2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("harry poter")

#ex3
def describe_city(city,country="Israel"):
    print(f"{city} is in {country}")

describe_city("holon")

#ex4
import random

def is_equal(num):
    num1=random.randint(1,100)
    if(num1==num):
        print("success")
    else:
        print(f"fail num={num} random number={num1}")
num=50
if(num>0 and num<101):
    is_equal(num)

#ex5
def make_shirt(size="large",text="i love python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt()
make_shirt("medium")
make_shirt("small","no soup for you")

#ex6
def show_magicians(list):
    for name in list:
        print(name)

def make_great(list):
    for i in range(len(list)):
        list[i] += " the Great"

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)

#ex7
import random

def get_random_temp(season):
    if season == 'winter':
        return random.uniform(-10, 16)
    elif season == 'spring' or season == 'fall' or season == 'autumn':
        return random.uniform(10, 23)
    elif season == 'summer':
        return random.uniform(24, 40)
    else:
        return random.uniform(-10, 40)

def main():
    season = input("Enter a season: ").lower()
    temp = get_random_temp(season)
    print(f"The temperature is {temp}")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 23:
        print("It's a bit cool outside. You might want to bring a light jacket or sweater just in case.")
    elif temp < 32:
        print("Feels pleasant! Enjoy the nice weather and dress comfortably for outdoor activities.")
    else:
        print("It's getting pretty hot! Make sure to stay hydrated and wear light and breathable clothing.")

# Call the main function
main()

