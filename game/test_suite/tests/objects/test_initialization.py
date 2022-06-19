import unittest
from game.common.enums import ObjectType
from game.common.items.item import Item
from game.common.dispenser import Dispenser
from game.common.station import Station
from game.common.items.pizza import Pizza

class TestInitialization(unittest.TestCase):
    def setUp(self):

        self.item = Item(quality=4, worth=20)
        self.station = Station(item=Item(4,20), is_infested=False)
        self.dispenser = Dispenser()
        self.pizza = Pizza()


    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.station.object_type, ObjectType.station)
        self.assertEqual(self.pizza.object_type, ObjectType.pizza)

    def testDispenserInit(self):
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)


if __name__ == '__main__':
    unittest.main()
