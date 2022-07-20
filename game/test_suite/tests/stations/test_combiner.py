import unittest
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.combiner import Combiner


class TestCombiner(unittest.TestCase):
    def setUp(self):
        self.topping = Topping(quality=4, worth=20, topping_type=ToppingType.peppers, is_cut=True)
        self.cheese = Topping(quality=4, worth=20, topping_type=ToppingType.cheese, is_cut=True)
        self.pizza = Pizza(state=PizzaState.sauced)
        self.combiner = Combiner()

    def testStorePizza(self):
        #store pizza
        test = self.combiner.take_action(self.pizza)
        self.assertIsNone(test)

    def testCheese(self):
        self.combiner.take_action(self.pizza)
        self.combiner.take_action(self.cheese)
        self.assertEqual(len(self.combiner.stored_pizza.toppings), 1)

    def testAddTopping(self):
        self.combiner.take_action(self.pizza)

        #add topping
        self.combiner.take_action(self.topping)
        self.assertEqual(len(self.combiner.stored_pizza.toppings), 0)

    def testTakePizza(self):
        test = self.combiner.take_action(self.pizza)
        self.assertIsNone(test)

        test = self.combiner.take_action(self.cheese)
        self.assertIsNone(test)
        self.assertEqual(len(self.combiner.stored_pizza.toppings), 1)

        test = self.combiner.take_action(self.topping)
        self.assertIsNone(test)

        #take pizza from station
        test = self.combiner.take_action(None)
        self.assertEqual(len(test.toppings), 2)
        self.assertIsNone(self.combiner.stored_pizza)


if __name__ == '__main__':
    unittest.main()