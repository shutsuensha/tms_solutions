from classes import Book, Library
from exceptions import *

library = Library()

try:
    book1 = Book(pages=300, year=2020, author="Author A", price=29.99)
    book2 = Book(pages=150, year=2018, author="Author B", price=19.99)
    book3 = Book(pages=200, year=2021, author="Author A", price=24.99)
except (ValidationError) as e:
    print(f"Ошибка при создании книги: {e}")


print(book1, book2, book3, sep='\n')

print('book1 дороже book2? - ', book1 > book2)
print('book2 дороже book3? - ', book2 > book3)
print('book3 дороже book1? - ', book3 > book1)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.get_book_info(1))
print(library.get_book_info(2))
print(library.get_book_info(3))

print(library.get_book_info(4)) # None

print(library.find_books_by_author('Author A'))
print(library.find_books_by_authors(['Author A', 'Author B']))

print(library)