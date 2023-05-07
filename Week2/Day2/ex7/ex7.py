# Ask the user to input their favorite fruits
favorite_fruits_str = input("Enter your favorite fruit(s), separated by a space: ")
favorite_fruits = favorite_fruits_str.split()

# Ask the user to input a fruit
chosen_fruit = input("Enter a fruit: ")

# Check if the chosen fruit is in the favorite fruits list
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")
