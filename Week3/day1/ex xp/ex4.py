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
