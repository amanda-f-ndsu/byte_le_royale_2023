
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *

class MovementController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, world, client):
        new_position = None
        if client.cook.chosen_action == ActionType.Move.up:
            if not world.game_map[client.cook.position[0]][client.cook.position[1]-1].occupied_by:
               new_position = (client.cook.position[0],client.cook.position[1]-1)
        if client.cook.chosen_action == ActionType.Move.down:
            if not world.game_map[client.cook.position[0]][client.cook.position[1]+1].occupied_by:
               new_position = (client.cook.position[0],client.cook.position[1]+1)
        if client.cook.chosen_action == ActionType.Move.left:
            if not world.game_map[client.cook.position[0]-1][client.cook.position[1]].occupied_by:
               new_position = (client.cook.position[0]-1,client.cook.position[1])
        if client.cook.chosen_action == ActionType.Move.right:
            if not world.game_map[client.cook.position[0]+1][client.cook.position[1]].occupied_by:
               new_position = (client.cook.position[0]+1,client.cook.position[1])
        if new_position:
            world.game_map[client.cook.position[0]][client.cook.position[1]].occupied_by = None
            client.cook.position = new_position
            world.game_map[client.cook.position[0]][client.cook.position[1]].occupied_by = client.cook


        
                         