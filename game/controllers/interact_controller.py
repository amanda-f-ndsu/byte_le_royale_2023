from turtle import position
from game.common.cook import Cook
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *
from game.common.stations.station import Station
from game.common.game_board import GameBoard
from game.common.stations.oven import Oven

class InteractController(Controller):

    def __init__(self):
        super().__init__()

    def handle_actions(self, cook, world):
        stat = None
        x = 0
        y = 0
        if isinstance(GameBoard.__init__().game_map[cook.position[0]][cook.position[1] - 1], Station):
            x = cook.position[0]
            y = cook.position[1] - 1
        elif isinstance(GameBoard.__init__().game_map[cook.position[0]][cook.position[1] + 1], Station):
            x = cook.position[0]
            y = cook.position[1] + 1
        elif isinstance(GameBoard.__init__().game_map[cook.position[0] - 1][cook.position[1]], Station):
            x = cook.position[0] - 1
            y = cook.position[1]
        elif isinstance(GameBoard.__init__().game_map[cook.position[0] + 1][cook.position[1]], Station):
            x = cook.position[0] + 1
            y = cook.positions[1]

        if(x == 0 and y == 0):
            stat = GameBoard.__init__().game_map[x][y]
            stat.take_action(cook)
