# Entry point for CLI

from lib.helpers import list_all_books, list_all_customers, rent_book, return_book, view_rentals

def menu():
    while True:
        print("\n📚 Welcome to BookNest CLI")
        print("1. View all books")
        print("2. View all customers")
        print("3. Rent a book")
        print("4. Return a book")
        print("5. View all rentals")
        print("6. Exit")
hahsgah
        choice = input("Enter choice: ")

        if choice == "1":
            list_all_books()
        elif choice == "2":
            list_all_customers()
        elif choice == "3":
            rent_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_rentals()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == '__main__':
    menu()
