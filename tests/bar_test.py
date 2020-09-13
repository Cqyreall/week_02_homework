import unittest

from src.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Wine", 200)
    
    def test_bar_has_drink(self):
        self.assertEqual("Wine", self.bar.name)
    
    def test_bar_has_price(self):
        self.assertEqual(200, self.bar.price)