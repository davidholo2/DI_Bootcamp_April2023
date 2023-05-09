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
