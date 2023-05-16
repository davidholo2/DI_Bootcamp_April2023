# ex1
from faker import Faker
from datetime import datetime
from datetime import date
import string
import random
import func

func.add_numbers(5, 5)

# func


def add_numbers(num1, num2):
    print(num1+num2)


# ex2


def guess(num):
    random_num = random.randint(1, 100)
    return (num == random_num)


print(guess(4))

# ex3


def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choices(letters, k=length))
    return random_string


random_string = generate_random_string(5)
print(random_string)

# ex4

today = date.today()
print("Today's date:", today)

# ex5


def time_until_january_1st():
    current_datetime = datetime.now()
    target_datetime = datetime(current_datetime.year + 1, 1, 1)
    time_left = target_datetime - current_datetime
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"The 1st of January is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours.")


time_until_january_1st()

# ex6


def minutes_lived(birthdate):
    current_datetime = datetime.now()
    age = current_datetime - birthdate
    minutes = age.total_seconds() / 60

    print(f"You have lived approximately {minutes:.2f} minutes.")


birthdate = datetime(2001, 7, 19)
minutes_lived(birthdate)

# ex7


def display_today_and_next_holiday():
    today = datetime.now()
    upcoming_holiday = datetime(2023, 6, 4)
    time_left = upcoming_holiday - today
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Today's date and time is: {today}")
    print(
        f"The next holiday is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours.")
    print("The next holiday is: Shavout")


display_today_and_next_holiday()

# ex8


def calculate_space_age(age_in_seconds):
    earth_year_seconds = 31557600

    planet_ratios = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    age_on_planets = {}

    for planet, ratio in planet_ratios.items():
        age_on_planets[planet] = round(
            age_in_seconds / (earth_year_seconds * ratio), 2)

    return age_on_planets


# Test the function
age_seconds = 1_000_000_000
age_on_planets = calculate_space_age(age_seconds)

for planet, age in age_on_planets.items():
    print(f"Age on {planet}: {age} Earth-years old")


# ex9

users = []


def add_user():
    fake = Faker()
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)


add_user()
add_user()
add_user()
for user in users:
    print(user)
