class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def oldest(list):
    max = list[0].age
    index = 0
    for i in range(1, len(list)):
        if (list[i].age > max):
            max = list[i].age
            index = i

    return list[index]


cats = []
for i in range(3):
    name = input("enter cats name: ")
    age = int(input("enter the age of the cat: "))
    cats.append(Cat(name, age))

oldest_cat = oldest(cats)
print(f"the oldest cat is {oldest_cat.name} and his is {oldest_cat.age}")
