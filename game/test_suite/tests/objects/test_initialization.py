import unittest
from game.common.cook import Cook
from game.common.enums import ObjectType, ActionType
from game.common.items.item import Item
from game.common.dispenser import Dispenser
from game.common.station import Station

class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, worth=20)
        self.cook = Cook(team="ACM", action=ActionType.test, item=self.item)
        self.dispenser = Dispenser()
        self.station = Station(item=Item(4,20), is_infested=False)
      
    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)
        self.assertEqual(self.station.object_type, ObjectType.station)
            
    def testCookInit(self):
        self.assertEqual(self.cook.chosen_action, ActionType.test)
        self.assertEqual(self.cook.object_type, ObjectType.cook)
        self.assertEqual(self.cook.held_item, self.item)

if __name__ == '__main__':
    unittest.main()