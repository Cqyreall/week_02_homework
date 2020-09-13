import unittest

from src.guest import Guest
from src.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Cyril", "Yes!", "VIP", 30000, "Dddudu")
        self.guest_2 = Guest("James", "Whoop!", "Regular", 800, "Perfect")
        self.room = Room("The Wonderland", 90, 400, 0)

    def test_guest_has_name(self):
        self.assertEqual("Cyril", self.guest_1.name)
    
    def test_guest_has_celebration(self):
        self.assertEqual("Yes!", self.guest_1.celebration)
    
    def test_guest_status(self):
        self.assertEqual("VIP", self.guest_1.status)
    
    def test_guest_has_wallet(self):
        self.assertEqual(30000, self.guest_1.wallet)
    
    def test_guest_has_paid_fee(self):
        self.guest_1.pay_fee(self.room)
        self.guest_2.pay_fee(self.room)
        self.assertEqual(29600, self.guest_1.wallet)
        self.assertEqual(710, self.guest_2.wallet)
    
    def test_guest_has_fav_song(self):
        self.assertEqual("Dddudu", self.guest_1.favourite_song)

    
