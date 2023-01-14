from game.common.cook import Cook
from game.common.enums import *
from game.common.game_board import GameBoard
from game.common.stations.station import Station
from game.common.stations.oven import Oven
from game.common.stations.roller import Roller
from game.common.stations.cutter import Cutter
from game.common.stations.storage import Storage
from game.common.stations.dispenser import Dispenser
from game.controllers.controller import Controller
from game.common.stations.Sauce import Sauce


class InteractController(Controller):

    def __init__(self):
        super().__init__()

    def handle_actions(self, client, world):
        if client.action.chosen_action is ActionType.interact:
            stat = None
            x = None
            y = None
            if isinstance(world.game_map[client.cook.position[1] - 1][client.cook.position[0]].occupied_by, Station):
                x = client.cook.position[0]
                y = client.cook.position[1] - 1
            elif isinstance(world.game_map[client.cook.position[1] + 1][client.cook.position[0]].occupied_by, Station):
                x = client.cook.position[0]
                y = client.cook.position[1] + 1
            elif isinstance(world.game_map[client.cook.position[1]][client.cook.position[0] - 1].occupied_by, Station):
                x = client.cook.position[0] - 1
                y = client.cook.position[1]
            elif isinstance(world.game_map[client.cook.position[1]][client.cook.position[0] + 1].occupied_by, Station):
                x = client.cook.position[0] + 1
                y = client.cook.position[1]
            if(x != None and y != None):
                stat = world.game_map[y][x].occupied_by
                return stat.take_action(client.cook)