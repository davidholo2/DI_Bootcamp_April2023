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
