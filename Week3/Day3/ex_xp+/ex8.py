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
