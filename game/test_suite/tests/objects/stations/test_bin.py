import unittest
from game.common.enums import *
from game.common.stations.bin import Bin
from game.common.items.item import Item
from game.common.cook import Cook


class TestBin(unittest.TestCase):

    def setUp(self) -> None:
        self.bin = Bin()
        self.item = Item(worth=2, quality=1)
        self.cook = Cook(action=ActionType.none, item=self.item)

    def test_bin_deletion(self):
        self.assertIsNotNone(self.cook.held_item)
        self.cook.held_item = self.bin.take_action(self.cook)
        self.assertIsNone(self.cook.held_item)


if __name__ == '__main__':
    unittest.main()
