import unittest
from game.common.enums import ObjectType
from game.common.items.item import Item
from game.common.dispenser import Dispenser


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, value=20)

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)

    def dispenserSetUp(self):
        self.dispenser = Dispenser()

    def testDispenserInit(self):
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)


if __name__ == '__main__':
    unittest.main()
