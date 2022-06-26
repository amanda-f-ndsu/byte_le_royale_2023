import unittest
from game.common.cook import Cook
from game.common.enums import ObjectType, ActionType
from game.common.items.item import Item
from game.common.dispenser import Dispenser
from game.common.map.tile import Tile
from game.common.station import Station
class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, worth=20)
        self.station = Station(item=Item(4,20), is_infested=False)
        self.dispenser = Dispenser()

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.station.object_type, ObjectType.station)

    def testDispenserInit(self):

        self.item = Item(quality=4, worth=20)
        self.cook = Cook(action=ActionType.test, item=self.item)
        self.dispenser = Dispenser()
        self.station = Station(item=Item(4,20), is_infested=False)
        self.tile = Tile(occupied_by= self.dispenser)
      
    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)

        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)
        self.assertEqual(self.station.object_type, ObjectType.station)
        self.assertEqual(self.tile.object_type, ObjectType.tile)
            
    def testCookInit(self):
        self.assertEqual(self.cook.chosen_action, ActionType.test)
        self.assertEqual(self.cook.object_type, ObjectType.cook)
        self.assertEqual(self.cook.held_item, self.item)

    def testTileInit(self):
        self.assertTrue(isinstance(self.tile.occupied_by, Dispenser))
        self.tile.occupied_by = self.cook
        self.assertTrue(isinstance(self.tile.occupied_by, Cook))
        self.tile.occupied_by = self.station
        self.assertTrue(isinstance(self.tile.occupied_by, Station))
        self.tile.occupied_by = self.item
        self.assertIsNone(self.tile.occupied_by)

if __name__ == '__main__':
    unittest.main()