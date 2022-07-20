
import unittest
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.roller import Roller


class TestBin(unittest.TestCase):

    def setUp(self) -> None:
        self.topping = Topping(quality=4, worth=20, topping_type=ToppingType.canadian_ham, is_cut=False)
        self.roller = Roller(self.topping)

    def testTakeAction(self):
        temp = self.roller.take_action(Topping(topping_type=ToppingType.dough))
        self.assertEqual(temp.object_type, ObjectType.pizza)

    def testNoActionOnHam(self):
        temp = self.roller.take_action(Topping(topping_type=ToppingType.canadian_ham))
        self.assertEqual(temp.object_type, ObjectType.topping)

    def testNoActionOnItem(self):
        temp = self.roller.take_action(Item(worth=1, quality=1))
        self.assertEqual(temp.object_type, ObjectType.item)

    def testNoActionOnNone(self):
        temp = self.roller.take_action(None)
        self.assertIsNone(temp)


if __name__ == '__main__':
    unittest.main()

