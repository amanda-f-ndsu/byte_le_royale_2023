import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.stations.Sauce import Sauce

class TestSauce(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza(state=PizzaState.rolled)
        self.sauced = Sauce()

    def test_pizza_false_State(self):
        # pizza state is not rolled
        self.pizza.state = PizzaState.baked
        self.pizza = self.sauced.take_action(Cook(item=self.pizza))
        self.assertIsNone(self.sauced.item)

    def test_pizza_false_Item(self):
        # item is not pizza
        itemFail = Item(quality=4, worth=20)
        self.pizza = self.sauced.take_action(Cook(item=itemFail))
        self.assertIsNone(self.sauced.item)

    def test_if_pizza__sauced(self):
        self.pizza.state = PizzaState.rolled
        self.sauced.take_action(Cook(item=self.pizza))
        self.assertEqual(self.pizza.state, PizzaState.sauced)

if __name__ == 'main':
    unittest.main()