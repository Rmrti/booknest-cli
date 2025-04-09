# Entry point for CLI

from lib.helpers import list_all_books, list_all_customers, rent_book, return_book, view_rentals

def menu():
    while True:
      
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
