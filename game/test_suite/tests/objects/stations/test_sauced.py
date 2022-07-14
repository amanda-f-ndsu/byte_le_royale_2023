import unittest
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.stations.Sauce import Sauce

class TestSauce(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza(state=PizzaState.rolled)
        self.sauced = Sauce()

    def test_pizza_false(self):
        # pizza state is not rolled
        self.pizza.state = PizzaState.none
        self.pizza = self.sauced.take_action(self.pizza)
        self.assertIsNone(self.sauced.item)
        # item is not pizza
        item = Item(quality=4, worth=20)
        self.pizza = self.oven.take_action(item)
        self.assertIsNone(self.sauced.item)

if __name__ == 'main':
    unittest.main()