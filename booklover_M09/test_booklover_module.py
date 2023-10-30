import unittest
from .booklover_module import booklover

class BookLoverTestSuite(unittest.TestCase):
   
    def test_1_add_book(self):
        obj1 = booklover("PersonOne", "PersonOne@email.com", "scifi")
        obj1.add_book("BookOne", 4)

    def test_2_add_book(self):
        obj2 = booklover("PersonTwo", "PersonTwo@email.com", "history")
        obj2.add_book("BookTwo", 5)
        obj2.add_book("BookTwo", 5)

    def test_3_has_read(self):
        obj3 = booklover("PersonThree", "PersonThree@email.com", "nonfiction")
        obj3.add_book("BookThree", 3)
        self.assertTrue(obj3.has_read('BookThree'), 'Test 3 failed!')
      
    def test_4_has_read(self):
        obj4 = booklover("PersonThree", "PersonThree@email.com", "nonfiction")
        self.assertFalse(obj4.has_read('BookFour'), 'Test 4 failed!')
      
    def test_5_num_books_read(self):
        obj5 = booklover("PersonFive", "PersonFive@email.com", "fiction")
        obj5.add_book("BookFive", 5)
        obj5.add_book("BookFour", 1)
        obj5.add_book("BookThree", 4)
        self.assertEqual(obj5.num_books_read(), 3, 'Test 5 failed!')
      
    def test_6_fav_books(self):
        obj6 = booklover("PersonSix", "PersonSix@email.com", "nonfiction")
        obj6.add_book("BookSix", 3)
        obj6.add_book("BookSeven", 5)
        obj6.add_book("BookEight", 4)
        self.assertTrue(obj6.book_list[obj6.book_list.book_rating > 3].shape[0] == 2, 'Test 6 failed!')

class testMe():
    testsuite = unittest.TestLoader().loadTestsFromTestCase(BookLoverTestSuite)
    unittest.TextTestRunner().run(testsuite)
    
if __name__ == '__main__':
    unittest.main(verbosity=3)