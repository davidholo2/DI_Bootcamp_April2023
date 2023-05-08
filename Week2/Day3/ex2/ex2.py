family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost=0
for name, age in family.items():
    if age < 3:
        print(f"{name} gets in for free.")
    elif 3 <= age <= 12:
        print(f"{name}'s ticket costs $10.")
        cost+=10
    else:
        print(f"{name}'s ticket costs $15.")
        cost+=15

print(cost)