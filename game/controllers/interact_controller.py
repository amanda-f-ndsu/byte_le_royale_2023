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
<<<<<<< HEAD
from game.common.stations.Sauce import Sauce
=======
from game.common.stations.sauce import Sauce
>>>>>>> 178d08184c392d29cef9e67c56c5ba54d608436b


class InteractController(Controller):

    def __init__(self):
        super().__init__()

<<<<<<< HEAD
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
<<<<<<< HEAD
            #breakpoint()
            stat = world.game_map[y][x].occupied_by
=======
            stat = world.game_map[x][y].occupied_by
>>>>>>> 178d08184c392d29cef9e67c56c5ba54d608436b
            return stat.take_action(cook)
=======
    def handle_actions(self, client, world):
        if client.action.chosen_action is ActionType.interact:
            stat = None
            x = None
            y = None
            if isinstance(world.game_map[client.cook.position[0] - 1][client.cook.position[1]].occupied_by, Station):
                x = client.cook.position[1]
                y = client.cook.position[0] - 1
            elif isinstance(world.game_map[client.cook.position[0] + 1][client.cook.position[1]].occupied_by, Station):
                x = client.cook.position[1]
                y = client.cook.position[0] + 1
            elif isinstance(world.game_map[client.cook.position[0]][client.cook.position[1] - 1].occupied_by, Station):
                x = client.cook.position[1] - 1
                y = client.cook.position[0]
            elif isinstance(world.game_map[client.cook.position[0]][client.cook.position[1] + 1].occupied_by, Station):
                x = client.cook.position[1] + 1
                y = client.cook.position[0]
            if(x != None and y != None):
                stat = world.game_map[y][x].occupied_by
<<<<<<< HEAD
                return stat.take_action(client.cook)
>>>>>>> 90e5653fc204fed8b6bc87eb355f5d31cbfa1773
=======
                result = stat.take_action(client.cook)
                client.cook.held_item = result
>>>>>>> 95696f9e6a05dc44a2416663155ad9787eabfde6
