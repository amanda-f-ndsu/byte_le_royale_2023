import unittest
from game.common.items.pizza import Pizza
from game.controllers.oven_controller import OvenController
from game.common.enums import *


class TestOvenController(unittest.TestCase):
    def setUp(self):
        self.ovenController = OvenController()
        self.pizza = Pizza()
        # self.oven = Oven()

    def test_oven_burned(self):
        pass

    def test_oven_cycle(self):
        pass

    def test_oven_baked(self):
        pass

    def test_oven_reset(self):
        pass
        
        