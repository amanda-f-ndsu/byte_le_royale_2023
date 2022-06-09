from game.common.enums import ActionType
from game.common.game_object import GameObject
from game.common.items.item import Item

class Cook(GameObject):
    def __init__(self, team: str, action:ActionType=ActionType.none, item:Item=None):
        super().__init__()
        self.team = team
        self.chosen_action = action
        self.held_item = item

    @property
    def team(self) -> str:
        return self.__team

    @property
    def chosen_action(self) -> ActionType:
        return self.__chosen_action

    @property
    def held_item(self) -> Item:
        return self.__held_item

    @team.setter
    def team(self, team:str):
        self.__team = team

    @chosen_action.setter
    def chosen_action(self, action:ActionType):
        self.__chosen_action = action

    @held_item.setter
    def held_item(self, item:Item):
        self.__held_item = item

    def to_json(self):
        data = super().to_json()
        data['team'] = self.team
        data['chosen_action'] = self.chosen_action
        data['held_item'] = self.held_item
        return data

    def from_json(self, data: dict) -> 'Cook':
        super().from_json(data)
        self.team = data['team']
        self.chosen_action= data['chosen_action']
        self.held_item = data['held_item'] 
        return self
