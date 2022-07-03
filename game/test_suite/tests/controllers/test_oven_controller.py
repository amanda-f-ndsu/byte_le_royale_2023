import unittest
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stats import GameStats
from game.controllers.oven_controller import OvenController
from game.common.enums import *


class TestOvenController(unittest.TestCase):
    def setUp(self):
        self.ovenController = OvenController()
        self.pizza = Pizza(PizzaState.sauced)
        self.pizza.add_topping(Topping(topping_type=ToppingType.cheese))
        self.oven = Oven()

    def test_oven_burned(self):
        self.oven.timer = 0
        self.pizza.state = PizzaState.baked
        self.oven.item = self.pizza
        self.ovenController.handle_actions(self.oven)
        self.assertIsNone(self.oven.item)
      

    def test_oven_cycle(self):
        pass

    def test_oven_baked(self):
        self.oven.timer = GameStats.oven_timer['baked']
        self.oven.item = self.pizza
        self.ovenController.handle_actions(self.oven)
        self.assertEqual(self.oven.item.state, PizzaState.baked)
        

    def test_oven_reset(self):
        self.oven.timer = GameStats.oven_timer['baked'] - 1
        self.ovenController.handle_actions(self.oven)
        self.assertEqual(self.oven.timer, 0)
        
        
        