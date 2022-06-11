
from game.common.items.item import Item
from game.common.station import Station
import unittest

class StationTest(unittest.TestCase): 

    def setUp(self): 
        self.station = Station(item=Item(4,20), is_infested=False)
    
    def test_dict_array(self): # Test methods should always start with the word 'test'
        a = self.d["array"]
        self.assertEqual(a, [1, 2, 3, 4, 5]) # The heart of a test method are assertions
        self.assertEqual(a[2], 3) # These methods take two arguments and compare them to one another
        self.assertIn(5, a) # There are loads of them, and they're all very useful
        

    def test_dict_string(self):
        s = self.d["string"]
        self.assertIn("Hello", s)
        self.assertNotEqual("Walkin' on the Sun", s)

    def test_dict_integer(self):
        i = self.d["integer"]
        self.assertGreater(50, i)
        self.assertAlmostEqual(i, 42.00000001) # Checks within 7 decimal points

    def test_dict_bool(self):
        b = self.d["bool"]
        self.assertFalse(b)
        self.assertEqual(b, False)

    # This is just the very basics of how to set up a test file
    # For more info: https://docs.python.org/3/library/unittest.html


if __name__ == '__main__':
    unittest.main
