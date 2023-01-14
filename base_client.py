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
        self.combiner_location = None
        self.tick = None
        self.oven = None

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
        if self.half == None:
            self.half = 0
            self.x_min = 1
            self.x_max = 5
            if cook.position[1] >= 6:
                self.half = 6
                self.x_min = 7
                self.x_max = 12

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
                    self.state = "Pizza_bare"
            case "Pizza_bare":
                sauce_location = self.scan_board(
                    world, ObjectType.sauce)
                if sauce_location and self.manhattan_distance(cook.position, sauce_location) > 1:
                    dist_tup = self.tuple_difference(cook.position, sauce_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                else:
                    action.chosen_action = ActionType.interact
                    self.state = "Sauced"
            case "Sauced":
                combiner_location = self.scan_board(
                    world, ObjectType.combiner)
                if combiner_location and self.manhattan_distance(cook.position, combiner_location) > 1:
                    dist_tup = self.tuple_difference(cook.position, combiner_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                else:
                    action.chosen_action = ActionType.interact
                    self.state = "combiner_pizza"
                    self.combiner_location = combiner_location
            case "combiner_pizza":
                cheese_location = self.scan_board(
                    world, ObjectType.dispenser, ToppingType.cheese)
                if cheese_location and self.manhattan_distance(cook.position, cheese_location) > 1:
                    dist_tup = self.tuple_difference(cook.position, cheese_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                elif cheese_location and self.manhattan_distance(cook.position, cheese_location) == 1:
                    action.chosen_action = ActionType.interact
                    self.state = "cut"
            case "cut":
                cutter = self.scan_board(
                    world, ObjectType.cutter)
                if cutter and self.manhattan_distance(cook.position, cutter) > 1:
                    dist_tup = self.tuple_difference(cook.position, cutter)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                elif cutter and self.manhattan_distance(cook.position, cutter) == 1:
                    action.chosen_action = ActionType.interact
                    self.state = "combiner_needs_cheese"
            case "combiner_needs_cheese":
                if  self.combiner_location and self.manhattan_distance(cook.position, self.combiner_location) > 1:
                    dist_tup = self.tuple_difference(cook.position,  self.combiner_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                else:
                    action.chosen_action = ActionType.interact
                    self.state = "combiner_has_cheese"
            case "combiner_has_cheese":
                action.chosen_action = ActionType.interact
                self.state = "uncooked"
                self.combiner_location = None
            case "uncooked":
                oven = self.scan_board(
                    world, ObjectType.oven)
                if oven and self.manhattan_distance(cook.position, oven) > 1:
                    dist_tup = self.tuple_difference(cook.position, oven)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                else:
                    action.chosen_action = ActionType.interact
                    self.oven = oven
                    self.state = "wait"
            case "wait":
                if world.game_map[self.oven[0]][self.oven[1]].occupied_by.item.state == PizzaState.baked:
                    action.chosen_action = ActionType.interact
                    self.state = "finished_pizza"
            case "finished_pizza":
                delivery_location = self.scan_board(
                    world, ObjectType.delivery)
                if delivery_location and self.manhattan_distance(cook.position, delivery_location) > 1:
                    dist_tup = self.tuple_difference(cook.position, delivery_location)
                    direction_to_move = self.decide_move(dist_tup)
                    action.chosen_action = direction_to_move
                else:
                    action.chosen_action = ActionType.interact
                    self.state = None
        pass

    def scan_board(self, world: GameBoard, object_type: ObjectType, topping_type: ToppingType = None) -> Tuple[int, int]:
        for y in range(0, len(world.game_map)):
            for x in range(self.half, len(world.game_map[y])):
                if world.game_map[y][x].occupied_by != None and world.game_map[y][x].occupied_by.object_type == object_type:
                    if topping_type is None or (world.game_map[y][x].occupied_by.item != None and world.game_map[y][x].occupied_by.item.topping_type == topping_type):
                        return (y, x)
        return None

    def manhattan_distance(self, int_tuple_one: Tuple[int, int], int_tuple_two : Tuple[int, int]) -> int:
        return abs(int_tuple_one[0] - int_tuple_two[0]) + abs(int_tuple_one[1] - int_tuple_two[1])

    def tuple_difference(self, int_tuple_one: Tuple[int, int], int_tuple_two : Tuple[int, int]) -> int:
        y_diff = (int_tuple_one[0] - max(min(int_tuple_two[0], self.y_max), self.y_min))
        x_diff = (int_tuple_one[1] - max(min(int_tuple_two[1], self.x_max), self.x_min))
        return (y_diff, x_diff)

    def decide_move(self, int_tuple : Tuple[int, int]) -> ActionType.Move:
        if int_tuple[1] > 0:
            return ActionType.Move.left
        elif int_tuple[1] < 0:
            return ActionType.Move.right
        elif int_tuple[0] > 0:
            return ActionType.Move.up
        elif int_tuple[0] < 0: 
            return ActionType.Move.down