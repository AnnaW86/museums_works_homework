import unittest
from models.work import Work
from models.museum import Museum

class TestWork(unittest.TestCase):
    
    def setUp(self):
        self.museum = Museum("Scottish National Gallery of Modern Art", "75 Belford Rd, EH4 3DR")
        self.work = Work("The Aficionado", "Pablo Picasso", 1936, self.museum)
    
    
    def test_work_has_title(self):
        self.assertEqual("The Aficionado", self.work.title)
        
        
    def test_work_has_artist(self):
        self.assertEqual("Pablo Picasso", self.work.artist)
       
        
    def test_work_has_year(self):
        self.assertEqual(1936, self.work.year)
    
    
    def test_work_get_details(self):
        self.assertEqual("The Aficionado by Pablo Picasso is in Scottish National Gallery of Modern Art", self.work.get_details())   