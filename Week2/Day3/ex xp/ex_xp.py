# ex1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dt = dict(zip(keys, values))
print(dt)

# ex2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost = 0
for name, age in family.items():
    if age < 3:
        print(f"{name} gets in for free.")
    elif 3 <= age <= 12:
        print(f"{name}'s ticket costs $10.")
        cost += 10
    else:
        print(f"{name}'s ticket costs $15.")
        cost += 15

print(cost)

# ex3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

print(brand)
brand["number_stores"] = 2
print(brand)
print(f"zara clients are how buy for {brand['type_of_clothes']}")
brand["country_creation "] = "Spain"
print(brand)
if ("international_competitors" in brand):
    brand["international_competitors"].append("Desigual")
print(brand)
del brand["creation_date"]
print(brand)
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print(brand)
print(brand["number_stores"])

# ex4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

dt1 = {}

for i, user in enumerate(users):
    dt1[user] = i
print(dt1)

dt2 = {}
for i, user in enumerate(users):
    dt2[i] = user
print(dt2)

users.sort()
dt3 = {}
for i, user in enumerate(users):
    dt3[user] = i
print(dt3)
