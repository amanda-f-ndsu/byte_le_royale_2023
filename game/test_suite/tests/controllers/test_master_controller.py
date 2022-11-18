import unittest
from game.common.enums import *
from game.common.player import Player
from game.common.stations.dispenser import Dispenser
from game.controllers.master_controller import MasterController
from game.utils.generate_game import generate_map


class TestDispenserController(unittest.TestCase):
    def setUp(self):
        self.masterController = MasterController()
        
    
    # def testElectrical(self):
    #     listofPlayers = { Player(),  Player()}

    #     self.masterController.event_active = EventType.electrical
    #     self.masterController.handle_events(listofPlayers, None)

    #     listOfOvens = self.masterController.current_world_data["game_map"].ovens() 
    #     #self.assertTrue(listOfOvens[0].is_powered, False)

    
   