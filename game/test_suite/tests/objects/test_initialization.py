import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.stations.dispenser import Dispenser
from game.common.stations.sauce import Sauce
from game.common.stations.roller import Roller
from game.common.stations.cutter import Cutter
from game.common.stations.combiner import Combiner
from game.common.map.tile import Tile
from game.common.stations.oven import Oven
from game.common.stations.storage import Storage
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.bin import Bin
from game.common.stations.delivery import Delivery
from game.common.game_board import GameBoard
from game.common.map.counter import Counter
from game.utils.generate_game import generate


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.item = Item(quality=1, worth=20)
        self.topping = Topping(quality=1, worth=20, topping_type=ToppingType.canadian_ham, is_cut=False)
        self.pizza = Pizza(state=PizzaState.rolled)
        self.dispenser = Dispenser()
        self.cook = Cook(item=self.item)
        self.tile = Tile(occupied_by= self.dispenser, is_wet_tile=True)
        self.sauce = Sauce(self.topping)
        self.tile = Tile(occupied_by=self.dispenser)
        self.cutter = Cutter(self.topping)
        self.roller = Roller(self.topping)
        self.bin = Bin()
        self.oven = Oven()
        self.storage = Storage()
        self.combiner = Combiner()
        self.delivery = Delivery()
        # self.station = Station() Can't instantiate abstract class

    def testObjectInit(self):
        self.assertEqual(self.cutter.object_type, ObjectType.cutter)
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.item.object_type, ObjectType.item)
        self.assertEqual(self.sauce.object_type, ObjectType.sauce)
        # self.assertEqual(self.station.object_type, ObjectType.station) Can't instantiate abstract class, manually checked
        self.assertEqual(self.roller.object_type, ObjectType.roller)
        self.assertEqual(self.dispenser.object_type, ObjectType.dispenser)
        self.assertEqual(self.topping.object_type, ObjectType.topping)
        self.assertEqual(self.tile.object_type, ObjectType.tile)
        self.assertEqual(self.oven.object_type, ObjectType.oven)
        self.assertEqual(self.storage.object_type, ObjectType.storage)
        self.assertEqual(self.bin.object_type, ObjectType.bin)
        self.assertEqual(self.combiner.object_type, ObjectType.combiner)
        self.assertEqual(self.delivery.object_type, ObjectType.delivery)

    def testCookInit(self):
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
        self.tile.occupied_by = self.storage
        self.assertTrue(isinstance(self.tile.occupied_by, Storage))
        self.tile.is_wet_tile = False
        self.assertFalse(self.tile.is_wet_tile)

    def testGameBoard(self):
        self.game_board = GameBoard(seed=1)
        temp = [
            [
                Counter(),
                Counter(),
                Oven(),
                Sauce(),
                Combiner(),
                Counter(),
                Counter(),
                Counter(),
                Combiner(),
                Sauce(),
                Oven(),
                Counter(),
                Counter()
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Bin(),
                None,
                None,
                Cook(position=(3, 3)),
                None,
                None,
                Delivery(),
                None,
                None,
                Cook(position=(9, 3)),
                None,
                None,
                Bin(),
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Counter(),
                Counter(),
                Cutter(),
                Oven(),
                Roller(),
                Counter(),
                Counter(),
                Counter(),
                Roller(),
                Oven(),
                Cutter(),
                Counter(),
                Counter()
            ]
        ]
        temp = [list(zip(map(lambda x: x.occupied_by, self.game_board.game_map[i]), temp[i])) for i in range(7)]
        for y in temp:
            for game_board_tile_occupied_by, temp_item in y:
                if not game_board_tile_occupied_by and not temp_item:
                    continue
                assert(isinstance(game_board_tile_occupied_by, temp_item.__class__))

        for i in self.game_board.cooks():
            assert (isinstance(i, Cook))

        t = self.game_board.cooks()
        t = t[0]
        if isinstance(t, Cook):
            t.held_item = self.topping

        t = self.game_board.cooks()
        t = t[0]
        if isinstance(t, Cook):
            assert(t.held_item.worth, self.topping.worth)

        for i in self.game_board.ovens():
            assert (isinstance(i, Oven))

if __name__ == '__main__':
    unittest.main()