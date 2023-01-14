from game.common.game_board import GameBoard
from game.common.stations.dispenser import Dispenser
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *

class DispenserController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, world : GameBoard, turn):
        for row in world.game_map:
            if isinstance(row[6].occupied_by,Dispenser):
                row[6].occupied_by.dispense(turn)
                         