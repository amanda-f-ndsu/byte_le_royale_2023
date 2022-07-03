import unittest
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.combiner import Combiner


class TestCombiner(unittest.TestCase):
    def setUp(self):
        self.topping = Topping(quality=4, worth=20, topping_type=ToppingType.peppers, is_cut=True)
        self.pizza = Pizza(state=PizzaState.sauced)
        self.combiner = Combiner()

    def testFunctions(self):
        #store pizza
        test = self.combiner.take_action(self.pizza)
        self.assertIsNone(test)

        #add topping
        test = self.combiner.take_action(self.topping)
        self.assertIsNone(test)

        #take pizza from station
        test = self.combiner.take_action(None)
        self.assertEqual(len(test.toppings), 1)
        self.assertIsNone(self.combiner.stored_pizza)

if __name__ == '__main__':
    unittest.main()