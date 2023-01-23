import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.oven import Oven


class TestOven(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza(state=PizzaState.sauced)
        self.oven = Oven()

    def test_take_pizza(self):
        self.pizza.add_topping(Topping(topping_type=ToppingType.cheese))
        self.pizza = self.oven.take_action(Cook(item=self.pizza))
        self.assertIsNone(self.pizza)
        self.assertTrue(isinstance(self.oven.item, Pizza))

    def test_return_pizza(self):
        self.pizza.state = PizzaState.baked
        self.pizza.add_topping(Topping(topping_type=ToppingType.cheese))
        self.oven.item = self.pizza
        item = self.oven.take_action(Cook(item=None))
        self.assertIsNone(self.oven.item)
        self.assertTrue(isinstance(item, Pizza))
    
    def take_pizza_false(self):
        # pizza state is not sauced
        self.pizza.state = PizzaState.rolled
        self.pizza = self.oven.take_action(Cook(item=self.pizza))
        self.assertIsNone(self.oven.item)
        # pizza has no toppings
        self.pizza.state = PizzaState.sauced
        self.assertIsNone(self.oven.item)
        # item is not pizza
        item_false = Item(quality=1, worth=20)
        self.pizza = self.oven.take_action(Cook(item=item_false))
        self.assertIsNone(self.oven.item)
    
    def test_double_pizza(self):
        self.pizza.add_topping(Topping(topping_type=ToppingType.cheese))
        self.pizza.add_topping(Topping(topping_type=ToppingType.anchovies))
        self.pizza = self.oven.take_action(Cook(item=self.pizza))
        # accepts first pizza
        self.assertIsNone(self.pizza)
        self.pizza = Pizza(state=PizzaState.sauced)
        self.pizza.add_topping(Topping(topping_type=ToppingType.cheese))
        self.pizza = self.oven.take_action(Cook(item=self.pizza))
        # makes sure pizzas didn't change in oven or in cook's hand
        self.assertTrue(len(self.oven.item.toppings) == 2)
        self.assertTrue(len(self.pizza.toppings) == 1)


if __name__ == '__main__':
    unittest.main()
