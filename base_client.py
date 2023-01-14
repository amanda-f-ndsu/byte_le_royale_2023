from typing import Tuple
from game.client.user_client import UserClient
from game.common.cook import Cook
from game.common.game_board import GameBoard
from game.common.action import Action
from game.common.cook import Cook
from typing import Tuple
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.state = None

    def team_name(self):
        """
        Allows the team to set a team name.
        :return: Your team name
        """
        return 'Sean\'s client'

    # This is where your AI will decide what to do
    def take_turn(self, turn : int, action : Action, world : GameBoard, cook : Cook):
        """
        This is where your AI will decide what to do.
        :param turn:        The current turn of the game.
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        match(self.state):
            case None:
                dough_location = self.scan_board(
                    world, ObjectType.dispenser, ToppingType.dough)
                if dough_location and self.manhattan_distance(cook.position, dough_location) > 1:
                    dist_tup = self.tuple_difference(cook.position, dough_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                elif dough_location and self.manhattan_distance(cook.position, dough_location) == 1:
                    action.chosen_action = ActionType.interact
                    self.state = "Dough"
            case "Dough":
                roller_location = self.scan_board(
                    world, ObjectType.roller)
                if roller_location and self.manhattan_distance(cook.position, roller_location) > 1:
                    dist_tup = self.tuple_difference(cook.position, roller_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                else:
                    action.chosen_action = ActionType.interact
                    self.state = "Roller_fetch"
            case "Roller_fetch":
                action.chosen_action = ActionType.interact
                self.state = "Roller_fetch"

        pass

    def scan_board(self, world: GameBoard, object_type: ObjectType, topping_type: ToppingType = None) -> Tuple[int, int]:
        for x in range(0, len(world.game_map)):
            for y in range(0, len(world.game_map[x])):
                if world.game_map[x][y].occupied_by != None and world.game_map[x][y].occupied_by.object_type == object_type:
                    if ToppingType is None or (world.game_map[x][y].occupied_by.item != None and world.game_map[x][y].occupied_by.item.topping_type == topping_type):
                        return (x, y)
        return None

    def manhattan_distance(self, int_tuple_one: Tuple[int, int], int_tuple_two : Tuple[int, int]) -> int:
        return abs(int_tuple_one[0] - int_tuple_two[0]) + abs(int_tuple_one[1] - int_tuple_two[1])

    def tuple_difference(self, int_tuple_one: Tuple[int, int], int_tuple_two : Tuple[int, int]) -> int:
        return ((int_tuple_one[0] - int_tuple_two[0]) , (int_tuple_one[1] - int_tuple_two[1]))

    def decide_move(self, int_tuple : Tuple[int, int]) -> ActionType.Move:
        if int_tuple[1] > 1:
            return ActionType.Move.left
        elif int_tuple[1] < -1:
            return ActionType.Move.right
        elif int_tuple[0] >= 1:
            return ActionType.Move.up
        elif int_tuple[0] <= -1: 
            return ActionType.Move.down