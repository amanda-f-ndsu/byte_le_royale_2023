from typing import Tuple
from game.client.user_client import UserClient
from game.common.cook import Cook
from game.common.game_board import GameBoard
from game.common.action import Action
from game.common.cook import Cook
from typing import Tuple
from game.common.enums import *

# Different states for state machine
class State:
    WAITING_FOR_DOUGH = 0
    HAS_DOUGH = 1
    HAS_ROLLED = 2

# Main client class
class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.state = State.WAITING_FOR_DOUGH
        # What side and x and y bounds are we using (set in start)
        self.is_left_side = None
        self.x_min = None
        self.y_min = 1
        self.x_max = None
        self.y_max = 5

    def team_name(self):
        """
        Return your team name for the engine

        :returns:       Your team name
        """
        return 'Base Client 1'

    # Start function
    def start(self, action: Action, world: GameBoard, cook: Cook):
        """
        Run on the first turn by the take_turn() function

        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        self.check_side(cook)

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, action: Action, world: GameBoard, cook: Cook):
        """
        This is where your bot will decide what to do.

        :param turn:        The current turn of the game.
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        # Run the start function on turn 1
        if turn == 1:
            self.start(action, world, cook)
        # Check state machine
        if self.state == State.WAITING_FOR_DOUGH:
            # Filter by dispensers with a dough object
            dough_position = self.scan_board(world, ObjectType.dispenser, lambda x: x.item != None and x.item.topping_type == ToppingType.dough)
            # Move to dough
            if dough_position != None:
                man_dist = self.manhattan_distance(cook.position, dough_position)
                if man_dist > 1:
                    action.chosen_action = self.move_action(cook.position, dough_position)
                else:
                    action.chosen_action = ActionType.interact
                    self.state = State.HAS_DOUGH
        elif self.state == State.HAS_DOUGH:
            # Find a roller station
            roller_position = self.scan_board(world, ObjectType.roller)
            # Move to roller
            if roller_position != None:
                man_dist = self.manhattan_distance(cook.position, roller_position)
                if man_dist > 1:
                    action.chosen_action = self.move_action(cook.position, roller_position)
                else:
                    action.chosen_action = ActionType.interact
                    self.state = State.HAS_ROLLED
        elif self.state == State.HAS_ROLLED:
            # Find a garbage bin
            bin_position = self.scan_board(world, ObjectType.bin)
            # Move to bin
            if bin_position != None:
                man_dist = self.manhattan_distance(cook.position, bin_position)
                if man_dist > 1:
                    action.chosen_action = self.move_action(cook.position, bin_position)
                else:
                    action.chosen_action = ActionType.interact
                    self.state = State.WAITING_FOR_DOUGH

    def check_side(self, cook):
        if self.is_left_side != None:
            return
        if cook.position[1] < 6:
            print("Left")
            self.is_left_side = True
            self.x_min = 1
            self.x_max = 5
        else:
            self.is_left_side = False
            self.x_min = 7
            self.x_max = 11
            print("Right")

    def move_action(self, cook_position: Tuple[int, int], target_location: Tuple[int, int]) -> ActionType.Move:
        """
        Determines which direction to move, and returns that ActionType
        """
        dist_tup = self.move_difference(cook_position, target_location)
        direction_to_move = self.decide_move(dist_tup)
        return direction_to_move

    def scan_board(self, world: GameBoard, station_type: ObjectType, item_type_eval_func=None) -> Tuple[int, int]:
        """
        Scans every tile on your clients half of the gameboard for a certain ObjectType enum
        topping_type_eval_func is a function that takes an item and returns True if you want that item
        If topping_type_eval_func isn't provided, it will just return the first Object found 
        Returns the position of what you were searching for
        """
        # For each tile on your side
        for y in range(self.y_min-1, self.y_max+2):
            for x in range(self.x_min-1, self.x_max+2):
                # Filter out things not of object type
                station = world.game_map[y][x].occupied_by
                if station != None and station.object_type == station_type:
                    item = station.item
                    # If not eval function, return the station
                    if item_type_eval_func == None:
                        return (y, x)
                    # Check eval function on item
                    elif item_type_eval_func(station):
                        return (y, x)
        # Didn't find anything that matched our criteria
        return None

    def manhattan_distance(self, int_tuple_one: Tuple[int, int], int_tuple_two: Tuple[int, int]) -> int:
        """
        See https://en.wikipedia.org/wiki/Taxicab_geometry
        """
        return abs(int_tuple_one[0] - int_tuple_two[0]) + abs(int_tuple_one[1] - int_tuple_two[1])

    def move_difference(self, int_tuple_one: Tuple[int, int], int_tuple_two: Tuple[int, int]) -> int:
        """
        Returns the difference between two tuples
        Pinned to your side of the gameboard
        """
        print(str(int_tuple_one) + " : " + str(int_tuple_two), end = "\t\t")

        y = max(min(int_tuple_two[1], self.y_max), self.y_min)
        x = max(min(int_tuple_two[0], self.x_max), self.x_min)

        print(str(int_tuple_one) + " : " + str((y, x)), end="\t\t")

        y_diff = int_tuple_one[1] - y
        x_diff = int_tuple_one[0] - x
        return (y_diff, x_diff)

    def decide_move(self, tuple_diff: Tuple[int, int]) -> ActionType.Move:
        """
        Decides which direction to move in, based on a tuple difference
        """
        if tuple_diff[1] > 0:
            print("L")
            return ActionType.Move.left
        elif tuple_diff[1] < 0:
            print("R")
            return ActionType.Move.right
        elif tuple_diff[0] > 0:
            print("U")
            return ActionType.Move.up
        elif tuple_diff[0] < 0:
            print("D")
            return ActionType.Move.down
