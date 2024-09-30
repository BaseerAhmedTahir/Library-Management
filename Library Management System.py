# Library Management System

books = []
users = []
book_id_counter = 1
user_id_counter = 1

def add_book(title, author, genre):
    global book_id_counter
    book = {
        "id": book_id_counter,
        "title": title,
        "author": author,
        "genre": genre,
        "status": "Available"
    }
    books.append(book)
    book_id_counter += 1

def add_user(name):
    global user_id_counter
    user = {
        "id": user_id_counter,
        "name": name,
        "borrowed_books": []
    }
    users.append(user)
    user_id_counter += 1

def view_books():
    if not books:
        print("No books available in the library.")
        return
    print("All Books:")
    for book in books:
        print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")

def search_books(search_term):
    found_books = [book for book in books if (search_term.lower() in book['title'].lower() or 
                                                search_term.lower() in book['author'].lower() or 
                                                search_term.lower() in book['genre'].lower())]
    if found_books:
        print("Search Results:")
        for book in found_books:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")
    else:
        print("No books found matching the search criteria.")

def borrow_book(user_id, book_id):
    user = next((u for u in users if u['id'] == user_id), None)
    book = next((b for b in books if b['id'] == book_id), None)

    if user and book:
        if book['status'] == "Available":
            book['status'] = "Checked Out"
            user['borrowed_books'].append(book_id)
            print(f"You have borrowed \"{book['title']}\".")
        else:
            print(f"Sorry, the book \"{book['title']}\" is currently checked out.")
    else:
        print("Invalid user ID or book ID.")

def return_book(user_id, book_id):
    user = next((u for u in users if u['id'] == user_id), None)
    book = next((b for b in books if b['id'] == book_id), None)

    if user and book:
        if book_id in user['borrowed_books']:
            book['status'] = "Available"
            user['borrowed_books'].remove(book_id)
            print(f"You have returned \"{book['title']}\".")
        else:
            print("This book was not borrowed by you.")
    else:
        print("Invalid user ID or book ID.")

def view_available_books():
    available_books = [book for book in books if book['status'] == "Available"]
    if available_books:
        print("Available Books:")
        for book in available_books:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']}")
    else:
        print("No available books.")

def view_checked_out_books():
    checked_out_books = [book for book in books if book['status'] == "Checked Out"]
    if checked_out_books:
        print("Checked Out Books:")
        for book in checked_out_books:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']}")
    else:
        print("No checked out books.")

def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View available books")
        print("6. View checked out books")
        print("7. Add a book")
        print("8. Add a user")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")
        if choice == '1':
            view_books()
        elif choice == '2':
            search_term = input("Enter a title, author, or genre to search for: ")
            search_books(search_term)
        elif choice == '3':
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to borrow: "))
            borrow_book(user_id, book_id)
        elif choice == '4':
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to return: "))
            return_book(user_id, book_id)
        elif choice == '5':
            view_available_books()
        elif choice == '6':
            view_checked_out_books()
        elif choice == '7':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter book genre: ")
            add_book(title, author, genre)
            print(f"Book \"{title}\" added to the library.")
        elif choice == '8':
            name = input("Enter user name: ")
            add_user(name)
            print(f"User \"{name}\" added to the system.")
        elif choice == '9':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Sample Data
    add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    add_book("1984", "George Orwell", "Dystopian")
    add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    add_user("Ali")
    add_user("Ahmed")

    main_menu()
