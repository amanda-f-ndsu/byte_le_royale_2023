
import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.roller import Roller


class TestRoller(unittest.TestCase):

    def setUp(self) -> None:
        self.topping = Topping(quality=1, worth=20, topping_type=ToppingType.canadian_ham, is_cut=False)
        self.roller = Roller()

    def testTakeAction(self):
        self.topping.topping_type = ToppingType.dough
        temp = self.roller.take_action(Cook(item=self.topping))
        self.assertEqual(temp.object_type, ObjectType.pizza)

    def testNoActionOnHam(self):
        temp = self.roller.take_action(Cook(item=self.topping))
        self.assertEqual(temp.object_type, ObjectType.topping)

    def testNoActionOnItem(self):
        temp = self.roller.take_action(Cook(item=Item(worth=1, quality=1)))
        self.assertEqual(temp.object_type, ObjectType.item)

    def testNoActionOnNone(self):
        temp = self.roller.take_action(Cook(item=None))
        self.assertIsNone(temp)


if __name__ == '__main__':
    unittest.main()

