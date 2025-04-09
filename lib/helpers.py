# Helper functions for CLI operations
from lib.db.models import session, Customer, Book, Rental

def list_all_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(customer)

def list_all_books():
    books = session.query(Book).all()
    for book in books:
        print(book)

def rent_book():
    customer_id = input("Enter customer ID: ")
    book_id = input("Enter book ID: ")

    customer = session.get(Customer, int(customer_id))
    book = session.get(Book, int(book_id))

    if customer and book:
        rental = Rental(customer=customer, book=book)
        session.add(rental)
        session.commit()
        print(f"✅ {customer.name} has rented '{book.title}'")
    else:
        print("❌ Invalid customer or book ID.")

def return_book():
    rental_id = input("Enter rental ID to return: ")
    rental = session.get(Rental, int(rental_id))
    if rental:
        session.delete(rental)
        session.commit()
        print("✅ Book returned.")
    else:
        print("❌ Rental not found.")

def view_rentals():
    rentals = session.query(Rental).all()
    for rental in rentals:
        print(rental)
