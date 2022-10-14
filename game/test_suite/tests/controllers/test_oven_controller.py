import unittest

from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.oven import Oven
from game.common.stats import GameStats
from game.controllers.oven_controller import OvenController


class TestOvenController(unittest.TestCase):
    def setUp(self):
        self.ovenController = OvenController()
        self.pizza = Pizza(PizzaState.sauced)
        self.pizza.add_topping(Topping(topping_type=ToppingType.cheese))
        self.oven = Oven(is_active=True)

    def test_oven_burned(self):
        self.oven.timer = 0
        self.pizza.state = PizzaState.baked
        self.oven.item = self.pizza
        self.ovenController.handle_actions(self.oven)
        self.assertIsNone(self.oven.item)
      

    def test_oven_cycle(self):
        self.oven.item = self.pizza
        self.ovenController.handle_actions(self.oven)
        self.assertEqual(self.oven.timer, GameStats.oven_timer['start']-1)

    def test_oven_baked(self):
        self.oven.timer = GameStats.oven_timer['baked']
        self.oven.item = self.pizza
        self.ovenController.handle_actions(self.oven)
        self.assertEqual(self.oven.item.state, PizzaState.baked)
        

    def test_oven_reset(self):
        self.oven.timer = GameStats.oven_timer['baked'] - 1
        self.ovenController.handle_actions(self.oven)
        # oven should be empty
        self.assertIsNone(self.oven.item)
        # timer should be restarted
        self.assertEqual(self.oven.timer, GameStats.oven_timer['start'])
        # oven should be set to inactive
        self.assertFalse(self.oven.is_active)
        
        
        