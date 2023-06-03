from faker import Faker
from rent.models import Customer, Address
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()


fake = Faker()


def create_customers(number):
    for _ in range(number):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()
        city = fake.city()
        country = fake.country()

        address_obj = Address.objects.create(
            address=address,
            city=city,
            country=country
        )

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address_obj
        )
        customer.save()

    print(f"CREATED {number} Customers")


create_customers(100)
