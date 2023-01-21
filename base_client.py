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
        self.tick = None

    def team_name(self):
        """
        Allows the team to set a team name.
        :return: Your team name
        """
        return 'Sean\'s client'

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
        self.decide_action(action, world, cook)
        pass

    def decide_action(self, action: Action, world: GameBoard, cook: Cook):
        if self.state == None:
            self.attempt_move_to_next_state(
                action, world, cook, "Dough", ObjectType.dispenser, lambda x: x.item != None and x.item.topping_type == ToppingType.dough)
        elif self.state == "Dough":
            self.attempt_move_to_next_state(
                action, world, cook, "Pizza_bare", ObjectType.roller)
        elif self.state == "Pizza_bare":
            self.attempt_move_to_next_state(
                action, world, cook, "Sauced", ObjectType.sauce)
        elif self.state == "Sauced":
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_pizza", ObjectType.combiner)
        elif self.state == "combiner_pizza":
            self.attempt_move_to_next_state(action, world, cook, "cut", ObjectType.dispenser,
                                            lambda x: x.item != None and x.item.topping_type == ToppingType.cheese)
        elif self.state == "cut":
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_needs_cheese", ObjectType.cutter)
        elif self.state == "combiner_needs_cheese":
            self.attempt_move_to_next_state(action, world, cook, "combiner_has_cheese",
                                            ObjectType.combiner, lambda x: ToppingType.cheese not in x.item.toppings)
        elif self.state == "combiner_has_cheese":
            self.attempt_move_to_next_state(action, world, cook, "got_item", ObjectType.dispenser,
                                            lambda x: x.item != None and x.item.topping_type != ToppingType.dough)
        elif self.state == "got_item":
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_needs_item", ObjectType.cutter)
        elif self.state == "combiner_needs_item":
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_has_item", ObjectType.combiner, lambda x: x is not None)
        elif self.state == "combiner_has_item":
            action.chosen_action = ActionType.interact
            self.state = "uncooked"
        elif self.state == "uncooked":
            self.attempt_move_to_next_state(
                action, world, cook, "wait", ObjectType.oven, lambda x: x.item is None)
        elif self.state == "wait":
            for oven in world.ovens():
                if oven.item is not None and oven.item.state == PizzaState.baked:
                    self.state = "move_to_oven"
        elif self.state == "move_to_oven":
            for oven in world.ovens():
                if oven.item is not None and oven.item.state == PizzaState.baked:
                    self.attempt_move_to_next_state(
                        action, world, cook, "finished_pizza", ObjectType.oven, lambda x: x.id == oven.id)
        elif self.state == "finished_pizza":
            self.attempt_move_to_next_state(
                action, world, cook, None, ObjectType.delivery)

    def attempt_move_to_next_state(self, action: Action, world: GameBoard, cook: Cook,
                                   next_state: str, obj_type: ObjectType, top_type_eval=None):
        item_location = self.scan_board(
            world, obj_type, top_type_eval)
        if item_location:
            man_dist = self.manhattan_distance(
                cook.position, item_location)
            if man_dist > 1:
                action.chosen_action = self.move_action(
                    cook.position, item_location)
            elif man_dist == 1:
                action.chosen_action = ActionType.interact
                self.state = next_state

    def move_action(self, cook_position, station_location) -> ActionType.Move:
        dist_tup = self.tuple_difference(cook_position, station_location)
        direction_to_move = self.decide_move(dist_tup)
        return direction_to_move

    def scan_board(self, world: GameBoard, object_type: ObjectType, obj_eval_func=None) -> Tuple[int, int]:
        for y in range(0, len(world.game_map)):
            for x in range(self.half, len(world.game_map[y])):
                if world.game_map[y][x].occupied_by != None and world.game_map[y][x].occupied_by.object_type == object_type:
                    if obj_eval_func is None or (world.game_map[y][x].occupied_by != None and obj_eval_func(world.game_map[y][x].occupied_by)):
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
