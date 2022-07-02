import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.dispenser import Dispenser
from game.common.cutter import Cutter
from game.common.map.tile import Tile
from game.common.station import Station
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=4, worth=20)
        self.topping = Topping(quality=4, worth=20, topping_type=ToppingType.canadian_ham, is_cut=False)
        self.station = Station(item=Item(4,20), is_infested=False)
        self.pizza = Pizza(state=PizzaState.rolled)
        self.dispenser = Dispenser()
        self.cook = Cook(action=ActionType.test, item=self.item)
        self.tile = Tile(occupied_by=self.dispenser)
        self.cutter = Cutter(self.topping)

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.cutter.object_type, ObjectType.roller)
        self.assertEqual(self.cutter.item.object_type, ObjectType.topping)
        self.assertEqual(self.station.object_type, ObjectType.station)
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)
        self.assertEqual(self.station.object_type, ObjectType.station)
        self.assertEqual(self.topping.object_type, ObjectType.topping)
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

    def testTakeAction(self):
        self.topping = self.cutter.take_action(self.topping)
        self.assertEqual(self.topping.topping_type, ToppingType.canadian_ham)
        self.assertEqual(self.topping.is_cut, True)


if __name__ == '__main__':
    unittest.main()