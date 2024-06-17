import unittest
from library.book import Book
from library.library import Library


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1984", "George Orwell")
        self.book2 = Book("Brave New World", "Aldous Huxley")

    def test_integration(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)

        found_book = self.library.find_book_by_title("1984")
        self.assertEqual(found_book, self.book1)

        self.library.remove_book(self.book1)
        self.assertNotIn(self.book1, self.library.books)


if __name__ == '__main__':
    unittest.main()
