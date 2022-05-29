import unittest
from game.common.enums import ObjectType
from game.common.items.item import Item


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, value=20)

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)


if __name__ == '__main__':
    unittest.main()
