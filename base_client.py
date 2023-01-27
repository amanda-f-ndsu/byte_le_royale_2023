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
        self.half = None
        self.x_min = None
        self.y_min = 1
        self.x_max = None
        self.y_max = 5
        self.tick = None
        self.pizza_states = []
        self.index_offset = 0

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
        for state_index in range(len(self.pizza_states)):
            if state_index - self.index_offset < len(self.pizza_states):
                self.decide_action(action, world, cook, state_index - self.index_offset)
            if action.chosen_action != 0:
                break
        if len(self.pizza_states) == 0 or (self.pizza_states[0] == "wait" and len(self.pizza_states) < 2):
            self.pizza_states.append(None)
            self.decide_action(action, world, cook, len(self.pizza_states) - 1)
        if action.chosen_action == 0 and len(self.pizza_states) < 2:
            dist_tup = self.tuple_difference(cook.position, (3,6))
            direction_to_move = self.decide_move(dist_tup)
            action.chosen_action = direction_to_move
        self.index_offset = 0
        pass

    def decide_action(self, action: Action, world: GameBoard, cook: Cook, state_index):
        pizza_state = self.pizza_states[state_index]
        if pizza_state == None and cook.held_item == None:
            self.attempt_move_to_next_state(
                action, world, cook, "Dough",state_index, ObjectType.dispenser, lambda x: x.item != None and x.item.topping_type == ToppingType.dough)
        elif pizza_state == "Dough" and cook.held_item is not None and cook.held_item.topping_type == ToppingType.dough:
            self.attempt_move_to_next_state(
                action, world, cook, "Pizza_bare",state_index, ObjectType.roller)
        elif pizza_state == "Pizza_bare" and cook.held_item is not None and cook.held_item.state == PizzaState.rolled:
            self.attempt_move_to_next_state(
                action, world, cook, "Sauced",state_index, ObjectType.sauce)
        elif pizza_state == "Sauced" and cook.held_item.state == PizzaState.sauced:
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_pizza",state_index, ObjectType.combiner, lambda x: x.item == None)
        elif pizza_state == "combiner_pizza" and cook.held_item == None:
            self.attempt_move_to_next_state(action, world, cook, "cut",state_index, ObjectType.dispenser,
                                            lambda x: x.item != None and x.item.topping_type == ToppingType.cheese)
        elif pizza_state == "cut" and cook.held_item is not None and cook.held_item.topping_type == ToppingType.cheese:
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_needs_cheese",state_index, ObjectType.cutter)
        elif pizza_state == "combiner_needs_cheese" and cook.held_item is not None and cook.held_item.topping_type == ToppingType.cheese:
            self.attempt_move_to_next_state(action, world, cook, "combiner_cheese",state_index,
                                            ObjectType.combiner, lambda x: x.item != None and ToppingType.cheese not in x.item.toppings)
        elif pizza_state == "combiner_cheese" and cook.held_item == None:
            self.attempt_move_to_next_state(action, world, cook, "cut_item",state_index, ObjectType.dispenser,
                                            lambda x: x.item != None and x.item.topping_type not in [ToppingType.cheese, ToppingType.dough])
        elif pizza_state == "cut_item" and cook.held_item is not None and cook.held_item.topping_type != None:
            self.attempt_move_to_next_state(
                action, world, cook, "combiner_needs_item",state_index, ObjectType.cutter)
        elif pizza_state == "combiner_needs_item" and cook.held_item is not None and cook.held_item.topping_type != None:
            self.attempt_move_to_next_state(action, world, cook, "combiner_complete",state_index,
                                            ObjectType.combiner, lambda x: x.item != None and ToppingType.cheese not in x.item.toppings)
        elif pizza_state == "combiner_complete" and cook.held_item == None:
            action.chosen_action = ActionType.interact
            self.pizza_states[state_index] = "uncooked"
        elif pizza_state == "uncooked" and cook.held_item is not None and cook.held_item.object_type == ObjectType.pizza:
            self.attempt_move_to_next_state(
                action, world, cook, "wait",state_index, ObjectType.oven, lambda x: x.item is None)
        elif pizza_state == "wait":
            for oven in self.scan_board_list(world, ObjectType.oven, lambda x: x.item != None):
                if oven.item is not None and oven.item.state == PizzaState.baked and cook.held_item == None:
                    self.pizza_states[state_index] = "move_to_oven"
        elif pizza_state == "move_to_oven" and cook.held_item == None:
            for oven in self.scan_board_list(world, ObjectType.oven, lambda x: x.item != None):
                if oven.item is not None and oven.item.state == PizzaState.baked:
                    self.attempt_move_to_next_state(
                        action, world, cook, "finished_pizza",state_index, ObjectType.oven, lambda x: x.id == oven.id)
        elif pizza_state == "finished_pizza" and cook.held_item is not None and cook.held_item.object_type == ObjectType.pizza:
            self.attempt_move_to_next_state(
                action, world, cook, None, state_index, ObjectType.delivery)

    def attempt_move_to_next_state(self, action: Action, world: GameBoard, cook: Cook,
                                   next_state: str, state_index: int, obj_type: ObjectType, top_type_eval=None):
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
                if next_state != None:
                    self.pizza_states[state_index] = next_state
                else:
                    self.pizza_states.pop(state_index)
                    self.index_offset += 1

    def move_action(self, cook_position, station_location) -> ActionType.Move:
        dist_tup = self.tuple_difference(cook_position, station_location)
        direction_to_move = self.decide_move(dist_tup)
        return direction_to_move

    def scan_board(self, world: GameBoard, object_type: ObjectType, obj_eval_func=None) -> Tuple[int, int]:
        for y in range(0, self.y_max + 2):
            for x in range(self.half, self.x_max + 2):
                if world.game_map[y][x].occupied_by != None and world.game_map[y][x].occupied_by.object_type == object_type:
                    if obj_eval_func is None or (world.game_map[y][x].occupied_by != None and obj_eval_func(world.game_map[y][x].occupied_by)):
                        return (y, x)
        return None

    def scan_board_list(self, world: GameBoard, object_type: ObjectType, obj_eval_func=None):
        rtn = []
        for y in range(0, self.y_max + 2):
            for x in range(self.x_min, self.x_max + 2):
                if world.game_map[y][x].occupied_by != None and world.game_map[y][x].occupied_by.object_type == object_type:
                    if obj_eval_func is None or (world.game_map[y][x].occupied_by != None and obj_eval_func(world.game_map[y][x].occupied_by)):
                        rtn.append(world.game_map[y][x].occupied_by)
        return rtn

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
