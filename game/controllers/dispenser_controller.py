from game.common.stations.dispenser import Dispenser
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.map.tile import Tile
from game.common.enums import *

class DispenserController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, world):
        for row in world.game_map:
            if isinstance(row[6], Tile) and isinstance(row[6].occupied_by, Dispenser):
                row[6].occupied_by.dispense()
                         