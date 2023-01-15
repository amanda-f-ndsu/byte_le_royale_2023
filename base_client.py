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
        self.half = None
        self.x_min = None
        self.y_min = 1
        self.x_max = None
        self.y_max = 5

    def team_name(self):
        """
        Allows the team to set a team name.
        :return: Your team name
        """
        return 'Team 1 client'

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, action: Action, world: GameBoard, cook: Cook):
        """
        This is where your AI will decide what to do.
        :param turn:        The current turn of the game.
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        if self.half == None:
            self.half = 0
            self.x_min = 1
            self.x_max = 5
            if cook.position[1] >= 6:
                self.half = 6
                self.x_min = 7
                self.x_max = 12

        if self.state == None:
            dough_location = self.scan_board(
                world, ObjectType.dispenser, ToppingType.dough)
            if dough_location:
                man_dist = self.manhattan_distance(
                    cook.position, dough_location)
                if man_dist > 1:
                    action.chosen_action = self.move_action(
                        cook.position, dough_location)
                elif man_dist == 1:
                    action.chosen_action = ActionType.interact
                    self.state = "Dough"
        else:
            action.chosen_action = ActionType.interact

    def move_action(self, cook_position, station_location) -> ActionType.Move:
        dist_tup = self.tuple_difference(cook_position, station_location)
        direction_to_move = self.decide_move(dist_tup)
        return direction_to_move

    def scan_board(self, world: GameBoard, object_type: ObjectType, topping_type: ToppingType = None) -> Tuple[int, int]:
        for y in range(0, len(world.game_map)):
            for x in range(self.half, len(world.game_map[y])):
                if world.game_map[y][x].occupied_by != None and world.game_map[y][x].occupied_by.object_type == object_type:
                    if topping_type is None or (world.game_map[y][x].occupied_by.item != None and world.game_map[y][x].occupied_by.item.topping_type == topping_type):
                        return (y, x)
        return None

    def manhattan_distance(self, int_tuple_one: Tuple[int, int], int_tuple_two: Tuple[int, int]) -> int:
        return abs(int_tuple_one[0] - int_tuple_two[0]) + abs(int_tuple_one[1] - int_tuple_two[1])

    def tuple_difference(self, int_tuple_one: Tuple[int, int], int_tuple_two: Tuple[int, int]) -> int:
        y_diff = (
            int_tuple_one[0] - max(min(int_tuple_two[0], self.y_max), self.y_min))
        x_diff = (
            int_tuple_one[1] - max(min(int_tuple_two[1], self.x_max), self.x_min))
        return (y_diff, x_diff)

    def decide_move(self, int_tuple: Tuple[int, int]) -> ActionType.Move:
        if int_tuple[1] > 0:
            return ActionType.Move.left
        elif int_tuple[1] < 0:
            return ActionType.Move.right
        elif int_tuple[0] > 0:
            return ActionType.Move.up
        elif int_tuple[0] < 0:
            return ActionType.Move.down
