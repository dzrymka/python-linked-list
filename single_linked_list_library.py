class Book:
    def __init__(self, title):
        self.title = title
        self.next = None


class Visitor:
    def __init__(self, name):
        self.name = name
        self.books = None
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def borrow_book(self, visitor_name, book_title):
        if self.head is None:
            new_visitor = Visitor(visitor_name)
            new_book = Book(book_title)
            new_visitor.books = new_book
            self.head = new_visitor
        else:
            current_visitor = self.head
            while (
                current_visitor.next is not None
                and current_visitor.name != visitor_name
            ):
                current_visitor = current_visitor.next

            if current_visitor.name == visitor_name:
                new_book = Book(book_title)
                if current_visitor.books is None:
                    current_visitor.books = new_book
                else:
                    current_book = current_visitor.books
                    while current_book.next is not None:
                        current_book = current_book.next
                    current_book.next = new_book
            else:
                new_visitor = Visitor(visitor_name)
                new_book = Book(book_title)
                new_visitor.books = new_book
                current_visitor.next = new_visitor

        print(
            "Buku dengan judul '{}' dipinjam oleh pengunjung '{}'.".format(
                book_title, visitor_name
            )
        )

    def print_books(self, visitor_name):
        current_visitor = self.head
        while current_visitor is not None and current_visitor.name != visitor_name:
            current_visitor = current_visitor.next

        if current_visitor is None:
            print("Pengunjung dengan nama '{}' tidak ditemukan.".format(visitor_name))
        else:
            if current_visitor.books is None:
                print(
                    "Pengunjung dengan nama '{}' tidak meminjam buku.".format(
                        visitor_name
                    )
                )
            else:
                current_book = current_visitor.books
                print("Buku yang dipinjam oleh pengunjung '{}':".format(visitor_name))
                print("----------------------")
                while current_book is not None:
                    print("Judul Buku: {}".format(current_book.title))
                    current_book = current_book.next
                print("----------------------")


library = Library()

library.borrow_book("Freelys", "Python Programming")
library.borrow_book("Siti", "Data Structures")
library.borrow_book("Freelys", "Machine Learning")
library.borrow_book("Siti", "Algorithms")

library.print_books("Freelys")
library.print_books("Siti")
