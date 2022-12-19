
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
            if cook_x - 1 >= 0 and not world.game_map[cook_x - 1][cook_y].occupied_by:
               new_position = (cook_x-1,cook_y)
        if client.action.chosen_action == ActionType.Move.down:
            if cook_x + 1 <= len(world.game_map) and not world.game_map[cook_x+1][cook_y].occupied_by:
               new_position = (cook_x+1,cook_y)
        if client.action.chosen_action == ActionType.Move.left:
            if cook_y - 1 >= 0 and not world.game_map[cook_x][cook_y-1].occupied_by:
               new_position = (cook_x,cook_y-1)
        if client.action.chosen_action == ActionType.Move.right:
            if cook_y + 1 <= len(world.game_map[cook_x]) and not world.game_map[cook_x][cook_y+1].occupied_by:
               new_position = (cook_x,cook_y+1)
        if new_position:
            world.game_map[cook_x][cook_y].occupied_by = None
            client.cook.position = (new_position[1],new_position[0])
            world.game_map[new_position[0]][new_position[1]].occupied_by = client.cook


        
                         