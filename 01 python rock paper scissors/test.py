import unittest
from main import is_win

class TestRockPaperScissors(unittest.TestCase):
    def test_is_win(self):
        # Test cases for is_win function
        self.assertTrue(is_win('r', 's'))  # Rock should win against scissors
        self.assertTrue(is_win('s', 'p'))  # Scissors should win against paper
        self.assertTrue(is_win('p', 'r'))  # Paper should win against rock
        self.assertFalse(is_win('r', 'p'))  # Rock should lose against paper
        self.assertFalse(is_win('s', 'r'))  # Scissors should lose against rock
        self.assertFalse(is_win('p', 's'))  # Paper should lose against scissors
        self.assertFalse(is_win('l', 's'))  # Lizard should lose against scissors
        self.assertTrue(is_win('s', 'l'))   # Scissors should win against lizard
        self.assertTrue(is_win('l', 'p'))   # Lizard should win against paper
        self.assertFalse(is_win('p', 'l'))  # Paper should lose against lizard
        self.assertTrue(is_win('l', 'sp'))  # Lizard should win against Spock
        self.assertFalse(is_win('sp', 'l')) # Spock should lose against lizard
        self.assertTrue(is_win('sp', 'r'))  # Spock should win against rock
        self.assertFalse(is_win('r', 'sp')) # Rock should lose against Spock
        self.assertTrue(is_win('sp', 's'))  # Spock should win against scissors
        self.assertFalse(is_win('s', 'sp')) # Scissors should lose against Spock

if __name__ == '__main__':
    unittest.main()