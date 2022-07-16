import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.dispenser import Dispenser
from game.common.stations.Sauce import Sauce
from game.common.map.tile import Tile
from game.common.stations.oven import Oven
from game.common.stations.station import Station
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.bin import Bin


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, worth=20)
        self.topping = Topping(quality=4, worth=20, topping_type=0, is_cut=False)
        self.pizza = Pizza(state=PizzaState.rolled)
        self.dispenser = Dispenser()
        self.cook = Cook(action=ActionType.test, item=self.item)
        self.tile = Tile(occupied_by= self.dispenser)
<<<<<<< HEAD
        self.sauce = Sauce(self.topping)
=======
        self.bin = Bin()
>>>>>>> de7987ce842b35c87087336a84508a3cda56c579
        self.oven = Oven()

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
<<<<<<< HEAD
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.sauce.object_type, ObjectType.sauced)
        self.assertEqual(self.station.object_type, ObjectType.station)
=======
>>>>>>> de7987ce842b35c87087336a84508a3cda56c579
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)
        self.assertEqual(self.topping.object_type, ObjectType.topping)
        self.assertEqual(self.tile.object_type, ObjectType.tile)
        self.assertEqual(self.oven.object_type, ObjectType.oven)
        self.assertEqual(self.bin.object_type, ObjectType.bin)

    def testCookInit(self):
        self.assertEqual(self.cook.chosen_action, ActionType.test)
        self.assertEqual(self.cook.object_type, ObjectType.cook)
        self.assertEqual(self.cook.held_item, self.item)

    def testTileInit(self):
        self.assertTrue(isinstance(self.tile.occupied_by, Dispenser))
        self.tile.occupied_by = self.cook
        self.assertTrue(isinstance(self.tile.occupied_by, Cook))
        self.tile.occupied_by = self.oven
        self.assertTrue(isinstance(self.tile.occupied_by, Oven))
        self.tile.occupied_by = self.item
        self.assertIsNone(self.tile.occupied_by)


if __name__ == '__main__':
    unittest.main()