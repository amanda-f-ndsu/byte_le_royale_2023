import unittest
from game.common.enums import *
from game.common.map.tile import Tile
from game.common.stations.dispenser import Dispenser
from game.controllers.dispenser_controller import DispenserController


class TestOvenController(unittest.TestCase):
    def setUp(self):
        self.dispenserController = DispenserController()
        self.world = [[Tile()]*5,[Tile()]*5,[Tile()]*5,[Tile()]*5,[Tile(occupied_by=Dispenser())]*5,
        [[Tile()]*5],[Tile()]*5,[Tile()]*5,[Tile()]*5,[Tile()]*5]
    
    def testTakeAction(self):
        for dispenser in self.world[4]:
            self.assertIsNone(dispenser.occupied_by.item)
        self.dispenserController.handle_actions(self.world)
        for dispenser in self.world[4]:
            self.assertIsNotNone(dispenser.occupied_by.item)
    
   