import json

class LibraryManager:
    def __init__(self):
        self.books = []
        self.load_library()

    def load_library(self):
        try:
            with open('library.txt', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print("Error loading library. Starting with an empty library.")
            self.books = []

    def save_library(self):
        with open('library.txt', 'w') as file:
            json.dump(self.books, file)

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        publication_year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'

        book = {
            'title': title,
            'author': author,
            'publication_year': publication_year,
            'genre': genre,
            'read_status': read_status
        }
        self.books.append(book)
        self.save_library()
        print(f"Book '{title}' added to the library.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                self.save_library()
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def search_book(self):
        search_term = input("Enter the title or author to search: ")
        results = [book for book in self.books if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
        
        if results:
            print("Search Results:")
            for book in results:
                self.display_book(book)
        else:
            print("No books found.")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("All Books in the Library:")
        for book in self.books:
            self.display_book(book)

    def display_book(self, book):
        read_status = "Read" if book['read_status'] else "Unread"
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['publication_year']}, Genre: {book['genre']}, Status: {read_status}")

    def display_statistics(self):
        total_books = len(self.books)
        if total_books == 0:
            print("No books in the library.")
            return
        read_books = sum(1 for book in self.books if book['read_status'])
        percentage_read = (read_books / total_books) * 100
        print(f"Total books: {total_books}, Percentage read: {percentage_read:.2f}%")

    def menu(self):
        while True:
            print("\nPersonal Library Manager")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_all_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_manager = LibraryManager()
    library_manager.menu()