import unittest
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.stations.storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza(state=PizzaState.sauced)
        self.storage = Storage()

    def test_take_pizza(self):
        self.pizza.add_topping(ToppingType.cheese)
        self.pizza = self.storage.take_action(self.pizza)
        self.assertIsNone(self.pizza)
        self.assertTrue(isinstance(self.storage.item, Pizza))

    def test_return_pizza(self):
        item = None
        self.pizza.state = PizzaState.baked
        self.pizza.add_topping(ToppingType.cheese)
        self.storage.item = self.pizza
        item = self.storage.take_action()
        self.assertIsNone(self.storage.item)
        self.assertTrue(isinstance(item, Pizza))
    
    




if __name__ == '__main__':
    unittest.main()