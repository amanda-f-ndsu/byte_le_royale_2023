from typing import Tuple
from game.client.user_client import UserClient
from game.common.cook import Cook
from game.common.game_board import GameBoard
from game.common.action import Action
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.state = None

        self.map_side = "R"

    def team_name(self):
        """
        Allows the team to set a team name.
        :return: Your team name
        """
        return 'Mitchell\'s client'

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, action: Action, world: GameBoard, cook: Cook):
        """
        This is where your AI will decide what to do.
        :param turn:        The current turn of the game.
        :param action:     This is the actions object that you will add effort allocations or decrees to.
        :param world:       Generic world information
        :param cook:        Your cook object to control
        """
        if cook.position[0] < 6:
            self.map_side = "L"
        else:
            self.map_side = "R"

        if self.map_side == "L":
            if not cook.held_item and world.game_map[cook.position[0] + 1][cook.position[1]] != ObjectType.dispenser:
                action.chosen_action = ActionType.Move.Right
            else
                action.chosen_action = ActionType.



