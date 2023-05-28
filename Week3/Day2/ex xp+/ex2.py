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
