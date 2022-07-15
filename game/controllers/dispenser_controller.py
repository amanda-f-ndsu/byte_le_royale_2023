from game.common.stations.dispenser import Dispenser
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *

class DispenserController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, world):
        for tile in world[int((GameStats.map_stats['width']/2)-1)]:
            if isinstance(tile.occupied_by,Dispenser):
                tile.occupied_by.dispense()
                         