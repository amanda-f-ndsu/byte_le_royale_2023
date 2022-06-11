import unittest
from game.common.enums import ObjectType
from game.common.items.item import Item

from game.common.station import Station

class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, worth=20)
        self.station = Station(item=Item(4,20), is_infested=False)

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.station.object_type, ObjectType.station)


if __name__ == '__main__':
    unittest.main()
