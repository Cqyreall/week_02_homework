import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("New man", "Ed sheeran")
    
    def test_song_name(self):
        self.assertEqual("New man", self.song.name)
    
    def test_song_has_verse(self):
        self.assertEqual("Ed sheeran", self.song.artist)