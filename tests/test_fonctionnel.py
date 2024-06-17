import unittest
from library.book import Book
from library.library import Library


class TestIntegration(unittest.TestCase):
    def test_library_integration(self):
        library = Library()
        
        # Create some books
        book1 = Book("1984", "George Orwell")
        book2 = Book("Brave New World", "Aldous Huxley")
        book3 = Book("Fahrenheit 451", "Ray Bradbury")

        # Add books to the library
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        # Verify books are added
        self.assertIn(book1, library.books)
        self.assertIn(book2, library.books)
        self.assertIn(book3, library.books)

        # List books and check output
        books_list = library.list_books()
        expected_list = [
            "1984 by George Orwell", 
            "Brave New World by Aldous Huxley", 
            "Fahrenheit 451 by Ray Bradbury"
        ]
        self.assertEqual(sorted(books_list), sorted(expected_list))

        # Find a book by title
        found_book = library.find_book_by_title("1984")
        self.assertEqual(found_book, book1)

        # Remove a book
        library.remove_book(book1)
        self.assertNotIn(book1, library.books)

        # Try to find the removed book
        found_book = library.find_book_by_title("1984")
        self.assertIsNone(found_book)

        # List books after removal
        books_list = library.list_books()
        expected_list = [
            "Brave New World by Aldous Huxley", 
            "Fahrenheit 451 by Ray Bradbury"
        ]
        self.assertEqual(sorted(books_list), sorted(expected_list))


if __name__ == '__main__':
    unittest.main()
