from faker import Faker

users = []


def add_user():
    fake = Faker()
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)


add_user()
add_user()
add_user()
for user in users:
    print(user)
