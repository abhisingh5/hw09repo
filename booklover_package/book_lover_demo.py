from booklover import BookLover

if __name__ == '__main__':
    bl = BookLover("A S", "as4@virginia", "genre")
    bl.add_book("Jane Eyre", 4)
    bl.add_book("War and Peace", 5)
    bl.add_book("The Great Gatsby", 3)
    print("Number of books read:", bl.num_books_read())