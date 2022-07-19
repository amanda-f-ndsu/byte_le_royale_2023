from os import stat
import unittest
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.delivery import Delivery
from game.common.stats import GameStats
from game.common.cook import Cook
import math

"""
Can't
-Dough
-Rolled
-Sauced

Can Pass
-Baked
-Only cheese
-Multiple toppings
"""


class TestDelivery(unittest.TestCase):
    def setUp(self):
        self.dough = Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.dough]["score"], topping_type=ToppingType.dough)
        self.rolled = Pizza(state=PizzaState.rolled)
        self.sauced = Pizza(state=PizzaState.sauced)
        self.baked = Pizza(quality=1.0, state=PizzaState.baked)
        self.baked.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.cheese]["score"], topping_type=ToppingType.cheese, is_cut=True))
        self.multiple = Pizza(quality=1.0, state=PizzaState.baked)
        self.baked.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.cheese]["score"], topping_type=ToppingType.cheese, is_cut=True))
        self.multiple.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.sausage]["score"], topping_type=ToppingType.sausage, is_cut=True))
        self.multiple.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.mushrooms]["score"], topping_type=ToppingType.mushrooms, is_cut=True))
        self.multiple.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.olives]["score"], topping_type=ToppingType.olives, is_cut=True))
        self.quality = Pizza(quality=1.0, state=PizzaState.baked)
        self.baked.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.cheese]["score"], topping_type=ToppingType.cheese, is_cut=True))
        self.quality.add_topping(Topping(quality=0.5, worth=GameStats.topping_stats[ToppingType.sausage]["score"], topping_type=ToppingType.sausage, is_cut=True))
        self.quality.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.mushrooms]["score"], topping_type=ToppingType.mushrooms, is_cut=True))
        self.quality.add_topping(Topping(quality=1.0, worth=GameStats.topping_stats[ToppingType.olives]["score"], topping_type=ToppingType.olives, is_cut=True))
        self.delivery = Delivery()

    def testJustDough(self):
        test = self.delivery.take_action(Cook(item=self.dough))
        self.assertTrue(test is self.dough)

    def testJustRolled(self):
        test = self.delivery.take_action(Cook(item=self.rolled))
        self.assertTrue(test is self.rolled)

    def testJustSauced(self):
        test = self.delivery.take_action(Cook(item=self.sauced))
        self.assertTrue(test is self.sauced)

    def testIfTakesBaked(self):
        test = self.delivery.take_action(Cook(item=self.baked))
        self.assertIsNone(test)

    def testIfTakesMultipleToppings(self):
        test = self.delivery.take_action(Cook(item=self.multiple))
        self.assertIsNone(test)

    def testScoreBaked(self):
        cook = Cook(item=self.baked)
        self.delivery.take_action(cook)
        self.assertEqual(cook.score, GameStats.topping_stats[ToppingType.dough]["score"] + GameStats.topping_stats[ToppingType.cheese]["score"])

    def testScoreMultiple(self):
        cook = Cook(item=self.multiple)
        self.delivery.take_action(cook)
        self.assertEqual(cook.score, GameStats.topping_stats[ToppingType.dough]["score"] + GameStats.topping_stats[ToppingType.cheese]["score"] + GameStats.topping_stats[ToppingType.sausage]["score"] + GameStats.topping_stats[ToppingType.mushrooms]["score"] + GameStats.topping_stats[ToppingType.olives]["score"])

    def testScoreQuality(self):
        cook = Cook(item=self.quality)
        self.delivery.take_action(cook)
        self.assertEqual(cook.score, GameStats.topping_stats[ToppingType.dough]["score"] + GameStats.topping_stats[ToppingType.cheese]["score"] + (int)(math.floor(GameStats.topping_stats[ToppingType.sausage]["score"] * 0.5)) + GameStats.topping_stats[ToppingType.mushrooms]["score"] + GameStats.topping_stats[ToppingType.olives]["score"])


if __name__ == '__main__':
    unittest.main()