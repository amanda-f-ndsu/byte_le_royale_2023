import unittest
from game.common.enums import *
from game.controllers.dispenser_controller import DispenserController


class TestOvenController(unittest.TestCase):
    def setUp(self):
        self.dispenserController = DispenserController()
    
       