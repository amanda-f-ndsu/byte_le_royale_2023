
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *

class MovementController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, world, client):
        new_position = None
        cook_x = client.cook.position[1]
        cook_y = client.cook.position[0]
        if client.action.chosen_action == ActionType.Move.up:
            if not world.game_map[cook_y - 1][cook_x].occupied_by:
               new_position = (cook_y-1,cook_x)
        if client.action.chosen_action == ActionType.Move.down:
            if not world.game_map[cook_y+1][cook_x].occupied_by:
               new_position = (cook_y+1,cook_x)
        if client.action.chosen_action == ActionType.Move.left:
            if not world.game_map[cook_y][cook_x-1].occupied_by:
               new_position = (cook_y,cook_x-1)
        if client.action.chosen_action == ActionType.Move.right:
            if not world.game_map[cook_y][cook_x+1].occupied_by:
               new_position = (cook_y,cook_x+1)
        if new_position:
            world.game_map[cook_y][cook_x].occupied_by = None
            client.cook.position = new_position
            world.game_map[new_position[0]][new_position[1]].occupied_by = client.cook


        
                         