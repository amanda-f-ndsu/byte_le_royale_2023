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

    def handle_actions(self, cook, world):
        stat = None
        x = 0
        y = 0
        if isinstance(world.game_map[cook.position[1] - 1][cook.position[0]].occupied_by, Station):
            x = cook.position[0]
            y = cook.position[1] - 1
        elif isinstance(world.game_map[cook.position[1] + 1][cook.position[0]].occupied_by, Station):
            x = cook.position[0]
            y = cook.position[1] + 1
        elif isinstance(world.game_map[cook.position[1]][cook.position[0] - 1].occupied_by, Station):
            x = cook.position[0] - 1
            y = cook.position[1]
        elif isinstance(world.game_map[cook.position[1]][cook.position[0] + 1].occupied_by, Station):
            x = cook.position[0] + 1
            y = cook.position[1]
        if(x != 0 or y != 0):
            #if(isinstance(world.game_map[x][y].occupied_by, Oven)):
            #    stat = world.game_map[x][y].occupied_by
            #    cook.held_item = stat.take_action(cook)
            #elif(isinstance(world.game_map[x][y].occupied_by, Roller)):
            #    stat = world.game_map[x][y].occupied_by
            #    cook.held_item = stat.take_action(cook)                
            #elif(isinstance(world.game_map[x][y].occupied_by, Cutter)):
            #    stat = world.game_map[x][y].occupied_by
            #    cook.held_item = stat.take_action(cook)
            #    print(cook.held_item)
            #elif(isinstance(world.game_map[x][y].occupied_by, Storage)):
            #    stat = world.game_map[x][y].occupied_by
            #    cook.held_item = stat.take_action(cook)
            #elif(isinstance(world.game_map[x][y].occupied_by, Dispenser)):
            #   stat = world.game_map[x][y].occupied_by
            #    cook.held_item = stat.take_action(cook.held_item)
            #elif(isinstance(world.game_map[x][y].occupied_by, Sauce)):
            #    stat = world.game_map[x][y].occupied_by
            #    return stat.take_action(cook)
            breakpoint()
            if(isinstance(world.game_map[x][y].occupied_by, Dispenser)):
               stat : Dispenser = world.game_map[x][y].occupied_by
               return stat.take_action(cook.held_item)
            else:
                stat = world.game_map[x][y].occupied_by
                return stat.take_action(cook)