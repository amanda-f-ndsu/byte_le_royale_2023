from game.common.action import Action
from game.common.enums import *
from game.config import Debug


class UserClient:
    def __init__(self, action : Action = Action()):
        self.debug_level = DebugLevel.client
        self.debug = True
        
    def print(self, *args):
        if self.debug and Debug.level >= self.debug_level:
            print(f'{self.__class__.__name__}: ', end='')
            print(*args)

    def team_name(self):
        return "The Worst"

    def take_turn(self, turn, actions, world):
        raise NotImplementedError("Implement this in subclass")
