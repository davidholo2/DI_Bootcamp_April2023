# ex1
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

# ex2


class dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")


davids_dog = dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = dog("Teacup", 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if (davids_dog.height > sarahs_dog.height):
    print(davids_dog.name)
else:
    print(sarahs_dog.name)

# ex3


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# ex4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if (new_animal not in self.animals):
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} not found")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] not in sorted_animals:
                sorted_animals[animal[0]] = [animal]
            else:
                sorted_animals[animal[0]].append(animal)
        sorted_animals = dict(sorted(sorted_animals.items()))
        for i, animals in enumerate(sorted_animals.values(), start=1):
            if len(animals) == 1:
                print(f"{i}: {animals[0]}")
            else:
                print(f"{i}: {animals}")

    def get_groups(self):
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] not in sorted_animals:
                sorted_animals[animal[0]] = [animal]
            else:
                sorted_animals[animal[0]].append(animal)
        sorted_animals = dict(sorted(sorted_animals.items()))
        for letter, animals in sorted_animals.items():
            print(f"{letter}: {animals}")


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Lion")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
