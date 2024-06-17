import unittest
from library.book import Book
from library.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1984", "George Orwell")
        self.book2 = Book("Brave New World", "Aldous Huxley")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.remove_book(self.book1)
        self.assertNotIn(self.book1, self.library.books)

    def test_remove_book_not_in_library(self):
        with self.assertRaises(ValueError):
            self.library.remove_book(self.book1)

    def test_find_book_by_title(self):
        self.library.add_book(self.book1)
        found_book = self.library.find_book_by_title("1984")
        self.assertEqual(found_book, self.book1)

    def test_find_book_by_title_not_found(self):
        found_book = self.library.find_book_by_title("Nonexistent Book")
        self.assertIsNone(found_book)

    def test_list_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        books_list = self.library.list_books()
        expected_list = ["1984 by George Orwell", "Brave New World by Aldous Huxley"]
        self.assertEqual(sorted(books_list), sorted(expected_list))


if __name__ == '__main__':
    unittest.main()
