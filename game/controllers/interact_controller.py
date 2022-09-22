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
        if cook.position[1] == 1 or cook.postion[1] == 7:
            stat = GameBoard.__init__().game_map[cook.position[0]][cook.position[1] - 1]
            if isinstance(stat, Station):
                stat.take_action(cook)
        elif cook.position[1] == 5 or cook.postion[1] == 11:
            stat = GameBoard.__init__().game_map[cook.position[0]][cook.position[1] + 1]
            if isinstance(stat, Station):
                stat.take_action(cook)
        elif cook.position[0] == 1:
            stat = GameBoard.__init__().game_map[cook.position[0] - 1][cook.position[1]]
            if isinstance(stat, Station):
                stat.take_action(stat, Station)
        elif cook.position[0] == 5:
            stat = GameBoard.__init__().game_map[cook.position[0] + 1][cook.position[1]]
            if isinstance(stat, Station):
                stat.take_action(stat, Station)
        if isinstance(stat, Oven):
            Oven()
