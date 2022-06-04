import unittest
from game.common.enums import ObjectType
from game.common.items.item import Item
from game.common.map.tile import Tile


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, value=20)
        #can't test until Dispenser or Station is done
        self.tile = Tile()

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.tile.object_type, ObjectType.tile)


if __name__ == '__main__':
    unittest.main()
