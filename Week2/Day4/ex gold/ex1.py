import datetime

def get_age(year, month, day):
    today = datetime.date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

def can_retire(gender, date_of_birth):
    birth_year, birth_month, birth_day = map(int, date_of_birth.split("/"))
    age = get_age(birth_year, birth_month, birth_day)
    if gender == "m":
        retirement_age = 67
    elif gender == "f":
        retirement_age = 62
    else:
        raise ValueError("Invalid gender")
    return age >= retirement_age

# example usage
gender = input("Enter your gender (m/f): ")
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")
if can_retire(gender, date_of_birth):
    print("You can retire!")
else:
    print("Sorry, you can't retire yet.")
