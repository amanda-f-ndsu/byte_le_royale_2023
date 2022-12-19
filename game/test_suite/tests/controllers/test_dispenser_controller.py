import unittest
from game.common.enums import *
from game.common.map.tile import Tile
from game.common.stations.dispenser import Dispenser
from game.controllers.dispenser_controller import DispenserController
from game.utils.generate_game import generate_map


class TestDispenserController(unittest.TestCase):
    def setUp(self):
        self.dispenserController = DispenserController()
        board = generate_map(5)
        self.world = board
    
    def testTakeAction(self):
        for item in self.world.game_map:
            if(isinstance(item[6].occupied_by,Dispenser)):
                self.assertIsNone(item[6].occupied_by.item)
        self.dispenserController.handle_actions(self.world)
        for item in self.world.game_map:
            if(isinstance(item[6].occupied_by,Dispenser)):
                self.assertIsNotNone(item[6].occupied_by.item)
    
   