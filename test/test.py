import unittest

from io import StringIO
from test_base import captured_io,captured_output
import luh

class TestMyNthNumber(unittest.TestCase):
    
    def test_even_nth_numbers(self):
        output=luh.even_nth_numbers([1, 3, 15, 20, 4, 90, 100])
        self.assertEqual(output,[20, 4, 90, 100])
        self.assertNotEqual(output,[20, 90, 100])


    def test_odd_nth_numbers(self):
        output=luh.odd_nth_numbers([1, 3, 15, 20, 4, 90, 100])
        self.assertEqual(output,[1, 3, 15])

