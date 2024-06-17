import unittest
from library.book import Book


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("1984", "George Orwell")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")

    def test_book_str(self):
        book = Book("1984", "George Orwell")
        self.assertEqual(str(book), "1984 by George Orwell")

    def test_book_equality(self):
        book1 = Book("1984", "George Orwell")
        book2 = Book("1984", "George Orwell")
        book3 = Book("Brave New World", "Aldous Huxley")
        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)


if __name__ == '__main__':
    unittest.main()
