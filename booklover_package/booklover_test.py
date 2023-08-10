import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        bl = BookLover("John Doe", "john@example.com", "mystery")
        bl.add_book("Jane Eyre", 4)
        self.assertTrue(bl.has_read("Jane Eyre"))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl = BookLover("John Doe", "john@example.com", "mystery")
        bl.add_book("Jane Eyre", 4)
        bl.add_book("Jane Eyre", 3)
        self.assertEqual(bl.num_books_read(), 1)

    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        bl = BookLover("John Doe", "john@example.com", "mystery")
        bl.add_book("Jane Eyre", 4)
        self.assertTrue(bl.has_read("Jane Eyre"))

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl = BookLover("John Doe", "john@example.com", "mystery")
        bl.add_book("Jane Eyre", 4)
        self.assertFalse(bl.has_read("War and Peace"))

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        bl = BookLover("John Doe", "john@example.com", "mystery")
        bl.add_book("Jane Eyre", 4)
        bl.add_book("War and Peace", 5)
        bl.add_book("The Great Gatsby", 3)
        self.assertEqual(bl.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating > 3
        bl = BookLover("John Doe", "john@example.com", "mystery")
        bl.add_book("Jane Eyre", 4)
        bl.add_book("War and Peace", 5)
        bl.add_book("The Great Gatsby", 3)
        fav_books = bl.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)