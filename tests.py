import unittest
from index import number_to_string


class TestNumbersToString(unittest.TestCase):

    def test_numbers_to_string(self):
        self.assertEqual(number_to_string(1), "one")
        self.assertEqual(number_to_string(2), "two")
        self.assertEqual(number_to_string(26), "twenty six")
        self.assertEqual(number_to_string(128), "one hundred twenty eight")
        self.assertEqual(number_to_string(228), "two hundred twenty eight")
        self.assertEqual(number_to_string(1028), "one thousand twenty eight")
        self.assertEqual(number_to_string(2028), "two thousand twenty eight")
