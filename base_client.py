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
        return 'Base client 1'

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, action: Action, world: GameBoard, cook: Cook):
        """
        This is where your AI will decide what to do.
        :param turn:        The current turn of the game.
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        if self.half == None:
            # Determines which half of the board you're on
            self.half = 0
            self.x_min = 1
            self.x_max = 5
            if cook.position[1] >= 6:
                self.half = 6
                self.x_min = 7
                self.x_max = 12

        if self.state == None:
            dough_location = self.scan_board(
                world, ObjectType.dispenser, lambda x: x.topping_type == ToppingType.dough)
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

        pass

    def move_action(self, cook_position: Tuple[int, int], station_location: Tuple[int, int]) -> ActionType.Move:
        """
        Determines which direction to move, and returns that ActionType
        """
        dist_tup = self.tuple_difference(cook_position, station_location)
        direction_to_move = self.decide_move(dist_tup)
        return direction_to_move

    def scan_board(self, world: GameBoard, object_type: ObjectType, item_type_eval_func=None) -> Tuple[int, int]:
        """
        Scans every tile on your clients half of the gameboard for a certain ObjectType enum
        topping_type_eval_func is a function that takes an item and returns True if you want that item
        If topping_type_eval_func isn't provided, it will just return the first Object found 
        """
        for y in range(0, len(world.game_map)):
            for x in range(self.half, len(world.game_map[y])):
                if world.game_map[y][x].occupied_by != None and world.game_map[y][x].occupied_by.object_type == object_type:
                    if item_type_eval_func is None or (world.game_map[y][x].occupied_by.item != None and item_type_eval_func(world.game_map[y][x].occupied_by.item)):
                        return (y, x)
        return None

    def manhattan_distance(self, int_tuple_one: Tuple[int, int], int_tuple_two: Tuple[int, int]) -> int:
        """
        See https://en.wikipedia.org/wiki/Taxicab_geometry
        """
        return abs(int_tuple_one[0] - int_tuple_two[0]) + abs(int_tuple_one[1] - int_tuple_two[1])

    def tuple_difference(self, int_tuple_one: Tuple[int, int], int_tuple_two: Tuple[int, int]) -> int:
        """
        Returns the difference between two tuples
        Pinned to your side of the gameboard
        """
        y_diff = (
            int_tuple_one[0] - max(min(int_tuple_two[0], self.y_max), self.y_min))
        x_diff = (
            int_tuple_one[1] - max(min(int_tuple_two[1], self.x_max), self.x_min))
        return (y_diff, x_diff)

    def decide_move(self, tuple_diff: Tuple[int, int]) -> ActionType.Move:
        """
        Decides which direction to move in, based on a tuple difference
        """
        if tuple_diff[1] > 0:
            return ActionType.Move.left
        elif tuple_diff[1] < 0:
            return ActionType.Move.right
        elif tuple_diff[0] > 0:
            return ActionType.Move.up
        elif tuple_diff[0] < 0:
            return ActionType.Move.down
