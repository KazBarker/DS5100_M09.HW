from booklover_M09.booklover_module import booklover

bookDemo = booklover("Demo Dan", "Dan@email.com", "nonfiction")
bookDemo.add_book("Principia Mathematica", 5)
print(bookDemo.num_books_read())