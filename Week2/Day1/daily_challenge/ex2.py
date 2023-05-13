# Ask the user for their birthdate
birthdate = input("Please enter your birthdate (DD/MM/YYYY): ")

# Calculate the user's age
from datetime import date
today = date.today()
birthdate_obj = date(int(birthdate[-4:]), int(birthdate[3:5]), int(birthdate[:2]))
age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))

# Calculate the number of candles to add to the cake
last_digit = int(str(age)[-1])
candles = "i" * last_digit

# Generate the birthday cake using ASCII art
cake = f'''
       ___{'i'*last_digit}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''

# Print the cake with a personalized birthday message
print(cake)
print(f"Happy {age}th Birthday on {birthdate}!")
