# Script to seed initial database data
from faker import Faker
from .models import Book, Customer, Rental, session, Base, engine
import random

def seed_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    fake = Faker()

    customers = [Customer(name=fake.name(), email=fake.email()) for _ in range(5)]
    books = [
        Book(title=fake.catch_phrase(), author=fake.name(), genre=random.choice(['Fiction', 'Sci-Fi', 'Romance', 'Mystery']))
        for _ in range(10)
    ]

    session.add_all(customers + books)
    session.commit()

    rentals = [Rental(customer=random.choice(customers), book=random.choice(books)) for _ in range(5)]
    session.add_all(rentals)
    session.commit()

    print("✅ Database seeded with dummy data.")

if __name__ == '__main__':
    seed_data()
