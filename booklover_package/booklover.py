import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if not self.book_list['book_name'].isin([book_name]).any():
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print("{} is already in the book list.".format(book_name))

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]