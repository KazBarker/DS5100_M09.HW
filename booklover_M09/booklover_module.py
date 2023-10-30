import pandas as pd

class booklover():
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, book_rating):
        if not self.book_list[self.book_list.book_name == book_name].empty:
            print(self.name, ' has already read ', book_name)
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
             })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            print(book_name, ' has been added to the list.')

    def has_read(self, book_name):
        if not self.book_list[self.book_list.book_name == book_name].empty: return True
        else: return False
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return pd.DataFrame(self.book_list[self.book_list.book_rating > 3])

if __name__ == '__main__':
    test_object = booklover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("LOTR", 5)
    test_object.fav_books()
    

