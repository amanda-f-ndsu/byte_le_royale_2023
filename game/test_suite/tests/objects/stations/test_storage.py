import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.stations.storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza(state=PizzaState.sauced)
        self.storage = Storage()

    def test_take(self):
        self.pizza.add_topping(ToppingType.cheese)
        self.pizza = self.storage.take_action(Cook(item=self.pizza))
        self.assertIsNone(self.pizza)
        self.assertTrue(isinstance(self.storage.item, Pizza))

    def test_return(self):
        self.pizza.state = PizzaState.baked
        self.pizza.add_topping(ToppingType.cheese)
        self.storage.item = self.pizza
        item_rtn = self.storage.take_action(Cook(item=None))
        self.assertIsNone(self.storage.item)
        self.assertTrue(isinstance(item_rtn, Pizza))

    def test_swap(self):
        self.storage.item = self.pizza
        pizza2 = Pizza(state=PizzaState.baked)
        pizza1 = self.storage.take_action(Cook(item=pizza2))
        self.assertTrue(isinstance(self.storage.item, Pizza))
        self.assertTrue(isinstance(pizza1, Pizza))
    

if __name__ == '__main__':
    unittest.main()
