from dataclasses import dataclass, field
from typing import Optional
from exceptions import *


@dataclass(order=True)
class Book:
    book_id: Optional[int] = field(default=None, compare=False)
    pages: int = field(default=..., compare=False)
    year: int = field(default=..., compare=False)
    author: str = field(default=..., compare=False)
    price: float = field(default=...)

    def __post_init__(self):

        if not isinstance(self.pages, int) or\
                not isinstance(self.year, int) or\
                not isinstance(self.author, str) or\
                not isinstance(self.price, float):
            raise ValidationError("Тип не соответсвуйте определнному.")
        
        if self.pages <= 0:
            raise InvalidPageCountError("Количество страниц должно быть положительным числом.")
        if not (1000 <= self.year <= 2024):
            raise InvalidYearError("Год должен быть между 1000 и 2024.")
        if self.price < 0:
            raise InvalidPriceError("Цена не может быть отрицательной.")
        
    def __str__(self):
        return f"Book(id={self.book_id}, title='{self.author}', pages={self.pages}, year={self.year}, price={self.price})"
    

class Library:
    def __init__(self):
        self.books = {}
        self._next_id = 1

    def add_book(self, book: Book):
        book.book_id = self._next_id
        self.books[self._next_id] = book
        self._next_id += 1

    def get_book_info(self, book_id: int) -> Optional[Book]:
        return self.books.get(book_id, None)
    
    def find_books_by_author(self, author: str) -> list[Book]:
        return [book for book in self.books.values() if book.author == author]

    def find_books_by_authors(self, authors: list[str]) -> list[Book]:
        return [book for book in self.books.values() if book.author in authors]

    def __str__(self):
        return "\n".join(str(book) for book in self.books.values())