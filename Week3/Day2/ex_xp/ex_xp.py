# ex1
import random


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


bengal = Bengal('Bengie', 3)
chartreux = Chartreux('Charly', 4)
siamese = Siamese('Siam', 2)

all_cats = [bengal, chartreux, siamese]
sara_pets = Pets(all_cats)
sara_pets.walk()

# ex2


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return (f"{self.name} is barking")

    def run_speed(self):
        return (self.weight/self.age*10)

    def fight(self, other_dog):
        dog1 = self.run_speed()*self.weight
        dog2 = other_dog.run_speed()*other_dog.weight
        if (dog1 > dog2):
            return (f"{self.name} won the fight")
        elif (dog1 == dog2):
            return ("nobody won")
        else:
            return (f"{other_dog.name} won the fight")


dog1 = Dog('Fido', 3, 20)
dog2 = Dog('Rex', 5, 30)
dog3 = Dog('Max', 4, 25)

print(dog1.bark())  # Output: Fido is barking
print(dog2.run_speed())  # Output: 6.0
print(dog3.fight(dog1))  # Output: Max won the fight

# ex3


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return (f"{self.name} is barking")

    def run_speed(self):
        return (self.weight/self.age*10)

    def fight(self, other_dog):
        dog1 = self.run_speed()*self.weight
        dog2 = other_dog.run_speed()*other_dog.weight
        if (dog1 > dog2):
            return (f"{self.name} won the fight")
        elif (dog1 == dog2):
            return ("nobody won")
        else:
            return (f"{other_dog.name} won the fight")


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *dog_names):
        print(f"{' '.join(dog_names)} all play together")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs",
                  "shakes your hand", "plays dead"]
        if self.trained:
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet")


my_dog = PetDog("Buddy", 5, 30)
my_dog.train()
my_dog.do_a_trick()
