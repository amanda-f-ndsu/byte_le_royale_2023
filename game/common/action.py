from game.common.enums import *


class Action:
    def __init__(self, chosen_action = ActionType.none):
        self.object_type = ObjectType.action
        self.chosen_action = chosen_action

    @property
    def chosen_action(self) -> int:
        return self.__chosen_action

    @chosen_action.setter
    def chosen_action(self, action: int):
        if isinstance(action, int) or isinstance(action, float) or action is None:
            self.__chosen_action = action

    def to_json(self):
        data = dict()

        data['object_type'] = self.object_type
        data['chosen_action'] = self.chosen_action

        return data

    def from_json(self, data):
        self.object_type = data['object_type']
        self.chosen_action = data['chosen_action']

    def __str__(self):
        outstring = ''
        outstring += f'Chosen Action: {self.chosen_action}\n'

        return outstring
