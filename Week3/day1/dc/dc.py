class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal}: {count}\n"
        info += "\n\tE-I-E-I-0!"
        return info


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

# added functions


class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal_type, quantity in self.animals.items():
            info += f"{animal_type} : {quantity}\n"
        info += "\nE-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animal_types = self.get_animal_types()
        if len(animal_types) == 1:
            animal_str = animal_types[0]
        elif len(animal_types) == 2:
            animal_str = " and ".join(animal_types)
        else:
            animal_str = ", ".join(
                animal_types[:-1]) + f", and {animal_types[-1]}"
        return f"{self.name}'s farm has {animal_str}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
animal_types = macdonald.get_animal_types()
print(animal_types)
short_info = macdonald.get_short_info()
print(short_info)
