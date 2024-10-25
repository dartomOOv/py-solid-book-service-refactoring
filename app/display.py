from abc import ABC, abstractmethod

from app.book import Book


class BaseDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        ...


class ConsoleDisplay(BaseDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BaseDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])

# def display(self, display_type: str) -> None:
#     if display_type == "console":
#         print(self.content)
#     elif display_type == "reverse":
#         print(self.content[::-1])
#     else:
#         raise ValueError(f"Unknown display type: {display_type}")
