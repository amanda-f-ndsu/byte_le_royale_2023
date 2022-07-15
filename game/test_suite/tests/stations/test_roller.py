
import unittest
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.roller import Roller


class TestBin(unittest.TestCase):

    def setUp(self) -> None:
        self.topping = Topping(quality=4, worth=20, topping_type=ToppingType.canadian_ham, is_cut=False)
        self.roller = Roller(self.topping)

    def testTakeAction(self):
        # temp: Topping = Topping()
        # cast(self.roller.take_action(self.topping),temp)
        temp = self.roller.take_action(Topping(topping_type=ToppingType.dough))
        isinstance(temp, Pizza)
        self.assertEqual(temp.object_type, ObjectType.pizza)


if __name__ == '__main__':
    unittest.main()

