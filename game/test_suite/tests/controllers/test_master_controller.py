import unittest
from game.common.enums import *
from game.common.player import Player
from game.common.stations.dispenser import Dispenser
from game.controllers.master_controller import MasterController
from game.utils import generate_game
from game.utils.generate_game import generate_map


class TestMasterController(unittest.TestCase):
    def setUp(self):
        self.masterController = MasterController()
        temp = generate_game.generate_map()
        temp.event_active = EventType.electrical
        self.world = {
            "game_map": temp
        }
        
    
    def testElectrical(self):
        listofPlayers = { Player(),  Player()}
        self.masterController.current_world_data = self.world
        self.masterController.handle_events(listofPlayers)
        listOfOvens = self.masterController.current_world_data["game_map"].ovens() 
        self.assertFalse(listOfOvens[0].is_powered)

    
   