# ex1
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(
            f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"{self.last_name} Family Members:")
        for member in self.members:
            print(f" - {member['name']}")


members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
my_family = Family(members, 'Smith')
my_family.born(name='John', age=0, gender='Male')
print(my_family.members)
print(my_family.is_18('Michael'))
print(my_family.is_18('John'))
my_family.family_presentation()

# ex2


class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)

    def use_power(self, name):
        member = [m for m in self.members if m['name'] == name][0]
        if member['age'] >= 18:
            print(f"{name}'s power is {member['power']}.")
        else:
            raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(f"{member['incredible_name']} - {member['power']}")


members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
        'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
        'power': 'read minds', 'incredible_name': 'SuperWoman'}
]
the_incredibles = TheIncredibles(members, 'Parr')
the_incredibles.incredible_presentation()
the_incredibles.born(name='Jack', age=0, gender='Male', is_child=True,
                     power='Unknown Power', incredible_name='BabyJack')
the_incredibles.incredible_presentation()
