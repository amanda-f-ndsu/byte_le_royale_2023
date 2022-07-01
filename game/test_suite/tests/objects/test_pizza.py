import unittest
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping

class TestPizza(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza(state=PizzaState.none)


    def testPizzaStates(self):
        # test rolled
        self.pizza.state = PizzaState.rolled
        self.assertEqual(self.pizza.state, PizzaState.rolled)
        # test sauced
        self.pizza.state = PizzaState.sauced
        self.assertEqual(self.pizza.state, PizzaState.sauced)
        # test baked
        self.pizza.state = PizzaState.baked
        self.assertEqual(self.pizza.state, PizzaState.baked)
        # test invalid, should remain baked
        self.pizza.state = 5
        self.assertEqual(self.pizza.state, PizzaState.baked)
    
    # test cases where toppings should work accordingly
    def testPizzaToppingsTrue(self):
        self.pizza.state = PizzaState.sauced
        self.assertEqual(len(self.pizza.toppings), 0)
        self.pizza.add_topping(ToppingType.cheese)
        self.assertEqual(len(self.pizza.toppings), 1)
        self.pizza.add_topping(ToppingType.chicken)
        self.assertEqual(len(self.pizza.toppings), 2)

    # test cases where toppings can't be added
    def testPizzaToppingsFalse(self):
        # test adding topping to pizza that isn't sauced
        self.pizza.state = PizzaState.rolled
        self.pizza.add_topping(ToppingType.cheese)
        self.assertEqual(len(self.pizza.toppings), 0)
        self.pizza.state = PizzaState.baked
        self.pizza.add_topping(ToppingType.cheese)
        self.assertEqual(len(self.pizza.toppings), 0)
        # test adding dough to pizza
        self.pizza.state = PizzaState.sauced
        self.pizza.add_topping(ToppingType.cheese)
        self.pizza.add_topping(ToppingType.dough)
        self.assertEqual(len(self.pizza.toppings), 1)
        # test trying to add more than 4 toppings
        self.pizza.add_topping(ToppingType.olives)
        self.pizza.add_topping(ToppingType.mushrooms)
        self.pizza.add_topping(ToppingType.peppers)
        self.assertEqual(len(self.pizza.toppings), 4)
        self.pizza.add_topping(ToppingType.mushrooms)
        self.assertEqual(len(self.pizza.toppings), 4)



       
       
  

if __name__ == '__main__':
    unittest.main()