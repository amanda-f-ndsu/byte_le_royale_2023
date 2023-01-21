from game.client.user_client import UserClient
from game.common.cook import Cook
from game.common.game_board import GameBoard
from game.common.action import Action
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.moves_to_take = []

    def team_name(self):
        """
        Allows the team to set a team name.
        :return: Your team name
        """
        return 'Mitchell\'s Client'

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, action: Action, world: GameBoard, cook: Cook):
        """
        This is where your AI will decide what to do.
        :param turn:        The current turn of the game.
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        """
        self.setup_turn(cook, world)
        if len(self.moves_to_take) != 0:
            action.chosen_action = self.moves_to_take.pop(0)

        self.get_move_list(cook.position, self.ovens[0])


    def setup_turn(self, cook, world):
        self.get_cook_side(cook)
        self.get_cooking_stations(world)
        self.get_dispensers()

    def get_move_list(self, origin, destination):
        origin_y = origin[0]
        origin_x = origin[1]
        destination_y = destination[0]
        destination_x = destination[1]

        while (origin_y, origin_x) != (destination_y, destination_x):
            if origin_y < destination_y:
                self.moves_to_take.append(ActionType.Move.down)
                origin_y += 1
            elif origin_y > destination_y:
                self.moves_to_take.append(ActionType.Move.up)
                origin_y -= 1
            elif origin_x < destination_x:
                self.moves_to_take.append(ActionType.Move.right)
                origin_x += 1
            elif origin_x > destination_x:
                self.moves_to_take.append(ActionType.Move.left)
                origin_x -= 1

    def get_cooking_stations(self, world: GameBoard):
        self.ovens_goto = []
        self.ovens_actual = []
        self.cutter_goto = []
        self.cutter_actual = []
        self.roller_goto = []
        self.roller_actual = []
        self.sauce_goto = []
        self.sauce_actual = []
        self.combiner_goto = []
        self.combiner_actual = []
        if self.is_left_side:
            # Top row
            for x in range(2, 5):
                if world.game_map[0][x].occupied_by.object_type == ObjectType.oven:
                    self.ovens_goto.append((1, x))
                    self.ovens_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.cutter:
                    self.cutter_goto.append((1, x))
                    self.cutter_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.roller:
                    self.roller_goto.append((1, x))
                    self.roller_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.sauce:
                    self.sauce_goto.append((1, x))
                    self.sauce_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.combiner:
                    self.combiner_goto.append((1, x))
                    self.combiner_actual.append((0, x))
            # Bottom row
                if world.game_map[6][x].occupied_by.object_type == ObjectType.oven:
                    self.ovens_goto.append((5, x))
                    self.ovens_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.cutter:
                    self.cutter_goto.append((5, x))
                    self.cutter_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.roller:
                    self.roller_goto.append((5, x))
                    self.roller_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.sauce:
                    self.sauce_goto.append((5, x))
                    self.sauce_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.combiner:
                    self.combiner_goto.append((5, x))
                    self.combiner_actual.append((6, x))
        else:
            # Player on Right Side
            # Top row
            for x in range(2, 5):
                if world.game_map[0][x].occupied_by.object_type == ObjectType.oven:
                    self.ovens_goto.append((1, x))
                    self.ovens_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.cutter:
                    self.cutter_goto.append((1, x))
                    self.cutter_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.roller:
                    self.roller_goto.append((1, x))
                    self.roller_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.sauce:
                    self.sauce_goto.append((1, x))
                    self.sauce_actual.append((0, x))
                elif world.game_map[0][x].occupied_by.object_type == ObjectType.combiner:
                    self.combiner_goto.append((1, x))
                    self.combiner_actual.append((0, x))
            # Bottom row
                if world.game_map[6][x].occupied_by.object_type == ObjectType.oven:
                    self.ovens_goto.append((5, x))
                    self.ovens_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.cutter:
                    self.cutter_goto.append((5, x))
                    self.cutter_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.roller:
                    self.roller_goto.append((5, x))
                    self.roller_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.sauce:
                    self.sauce_goto.append((5, x))
                    self.sauce_actual.append((6, x))
                elif world.game_map[6][x].occupied_by.object_type == ObjectType.combiner:
                    self.combiner_goto.append((5, x))
                    self.combiner_actual.append((6, x))

    def get_dispensers(self):
        self.dispensers_actual = [(1, 6), (2, 6), (4, 6), (5, 6)]
        if self.is_left_side:
            self.dispensers_goto = [(1, 5), (2, 5), (4, 5), (5, 5)]
        else:
            self.dispensers_goto = [(1, 7), (2, 7), (4, 7), (5, 7)]

    def get_cook_side(self, cook: Cook):
        if cook.position[1] < 6:
            self.is_left_side = True
        else:
            self.is_left_side = False
