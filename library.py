class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

        # to make the text colorful
        # (please set up colorama in your machine in terminal with 'pip install colorama' command)
        from colorama import init, Fore
        init()
        self.Fore = Fore

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if books:

            for book in books:
                book_info = book.split(',')
                print(self.Fore.YELLOW + f"Book: {book_info[0]}, Author: {book_info[1]}" + self.Fore.RESET)
        else:
            print(self.Fore.RED + "No books available." + self.Fore.RESET)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        self.file.flush()
        print(self.Fore.GREEN + "✔ Book added successfully." + self.Fore.RESET)

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books = self.file.read().splitlines()

        updated_books = []
        removed = False

        for book in books:
            if title_to_remove.strip() != book.split(',')[0].strip():
                updated_books.append(book)
            else:
                removed = True

        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.write("\n".join(updated_books))
            print(self.Fore.GREEN + f"✔ Book '{title_to_remove}' removed successfully." + self.Fore.RESET)
        else:
            print(self.Fore.RED + f"Book '{title_to_remove}' not found." + self.Fore.RESET)


# to use the Library class
library = Library()


def print_menu():
    print("╔═════════════════════════════════════════╗")
    print("║             *** MENU ***                ║")
    print("╠═════════════════════════════════════════╣")
    print("║  1. List Books                          ║")
    print("║  2. Add Book                            ║")
    print("║  3. Remove Book                         ║")
    print("║  q. Exit                                ║")
    print("╚═════════════════════════════════════════╝")


while True:

    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n========== List Books ==========")
        library.list_books()
    elif choice == "2":
        library.add_book()
    elif choice == "3":
        library.remove_book()
    elif choice == "q":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
