import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("The Wonderland", 90, 400, 0)

        self.guest_1 = Guest("Cyril", "Yes!", "VIP", 30000, "Dddudu")
        self.guest_2 = Guest("Max", "Yayy", "Regular", 400, "Perfect")
        self.guest_3 = Guest("David", "Grmm", "VIP", 300, "See you again")
        self.guest_4 = Guest("Daniel", "Whoop", "VIP", 8000, "Gucci")

        self.song_1 = Song("Dddudu", "Blackpink")
        self.song_2 = Song("Perfect", "Ed sheeran")
        self.song_3 = Song("Gucci", "Jessie")

        red_wine = Bar("Red Wine", 300)
        jack_daniels = Bar("Jack Daniels", 200)
        johnny_walker = Bar("Johnny Walker", 400)
        water = Bar("Water", 10)
        
        self.vip_drinks = [{"Drink":red_wine, "quantity":9}, {"Drink":jack_daniels, "quantity":4}, {"Drink":johnny_walker, "quantity":5}, {"Drink":water, "quantity":50}]

    
    def test_name_of_room(self):
        self.assertEqual("The Wonderland", self.room.name)
    
    def test_room_has_fee(self):
        self.assertEqual(400, self.room.vip_fee)
    
    def test_room_fee(self):
        self.assertEqual(0, self.room.till)
    
    def test_guest_sorted(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.assertEqual(2, len(self.room.vip_guest))
        self.assertEqual(2, len(self.room.regular_guest))
    
    def test_checkout_guest(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.room.check_out_guest(self.guest_2)
        self.assertEqual(2, len(self.room.vip_guest))
        self.assertEqual(1, len(self.room.regular_guest))
    
    def test_song_added_to_list(self):
        self.room.add_songs(self.song_1)
        self.room.add_songs(self.song_2)
        self.assertEqual(2, len(self.room.songs))
    
    def test_minimize_number_of_guests(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_1)
        self.room.restrict_guest(self.guest_1)
        self.assertEqual(8, len(self.room.vip_guest))
        self.assertEqual(3, self.room.waiting_line)
    
    def test_minimize_number_of_regular_guests(self):
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_2)
        self.room.restrict_guest(self.guest_2)
        self.assertEqual(1, self.room.waiting_line)
    
    def test_room_till(self):
        self.guest_1.pay_fee(self.room)
        self.guest_2.pay_fee(self.room)
        self.assertEqual(490, self.room.till)
    
    def test_guest_cant_afford(self):
        self.room.guest_can_afford(self.guest_3)
        self.assertEqual(0, self.room.till)

    def test_guest_can_afford(self):
        self.room.guest_can_afford(self.guest_1)
        self.assertEqual(400, self.room.till)

    def test_guest_can_find_song_by_artist(self):
        self.room.add_songs(self.song_1)
        self.room.add_songs(self.song_2)
        self.assertEqual("Perfect",  self.room.guest_can_find_song(self.song_2.artist))
    
    def test_guest_favourite_song(self):
        self.room.add_songs(self.song_1)
        self.room.add_songs(self.song_2)
        self.room.add_songs(self.song_3)
        self.assertEqual("Yes!", self.room.play_song(self.guest_1))
        self.assertEqual("Nahhh", self.room.play_song(self.guest_3))
    
    def test_pub_add_drink(self):
        self.room.add_drink(self.vip_drinks[1])
        self.room.add_drink(self.vip_drinks[1])
        self.assertEqual(6, self.vip_drinks[1]["quantity"])
    
    def test_pub_remove_drink(self):
        self.room.add_drink(self.vip_drinks[2])
        self.room.add_drink(self.vip_drinks[2])
        self.room.remove_drink(self.vip_drinks[2])
        self.assertEqual(6, self.vip_drinks[2]["quantity"])
    
    def test_guest_sell_drink(self):
        self.guest_4.pay_fee(self.room)
        self.room.sell_drink(self.guest_4, self.vip_drinks[1])
        self.room.add_songs(self.song_3)
        self.assertEqual(600, self.room.till)
        self.assertEqual(3, self.vip_drinks[1]["quantity"])
        self.assertEqual(7400, self.guest_4.wallet)
        self.assertEqual("Whoop", self.room.play_song(self.guest_4))


    

