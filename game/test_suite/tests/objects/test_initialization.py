import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.dispenser import Dispenser
from game.common.stations.roller import Roller
from game.common.map.tile import Tile
from game.common.stations.oven import Oven
from game.common.stations.station import Station
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
        self.roller = Roller(self.topping)
        self.oven = Oven()

    def testObjectInit(self):
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.roller.object_type, ObjectType.roller)
        self.assertEqual(self.roller.item.object_type, ObjectType.topping)
        self.assertEqual(self.station.object_type, ObjectType.station)
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)
        self.assertEqual(self.station.object_type, ObjectType.station)
        self.assertEqual(self.topping.object_type, ObjectType.topping)
        self.assertEqual(self.tile.object_type, ObjectType.tile)
        self.assertEqual(self.oven.object_type, ObjectType.oven)
            
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
        # temp: Topping = Topping()
        # cast(self.roller.take_action(self.topping),temp)
        temp = self.roller.take_action(Topping(topping_type=ToppingType.dough))
        isinstance(temp, Pizza)
        self.assertEqual(temp.object_type, ObjectType.pizza)


if __name__ == '__main__':
    unittest.main()