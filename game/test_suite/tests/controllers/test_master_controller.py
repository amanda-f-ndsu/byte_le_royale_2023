import unittest
from game.common.enums import *

from game.common.stations.dispenser import Dispenser
from game.controllers.master_controller import MasterController
from game.utils.generate_game import generate_map


class TestDispenserController(unittest.TestCase):
    def setUp(self):
        self.masterController = MasterController()
        
    
    def testElectrical(self):
        
       self.masterController.event_active = EventType.electrical
       self.masterController.handle_events()
       self.masterController.current_world_data["game_map"].ovens() 


    
   