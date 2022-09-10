from game.common.enums import ActionType, ObjectType
from game.common.game_object import GameObject
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping



class Cook(GameObject):
    def __init__(self, action: ActionType = ActionType.none, item: Item = None, position: tuple = (0,0)):
        super().__init__()
        self.object_type = ObjectType.cook
        self.chosen_action = action
        self.held_item = item
        self.score = 0
        self.position = position

    @property
    def chosen_action(self) -> ActionType:
        return self.__chosen_action

    @property
    def held_item(self) -> Item:
        return self.__held_item

    @property
    def score(self) -> int:
        return self.__score

    @property
    def position(self) -> tuple:
        return self.__position

    @chosen_action.setter
    def chosen_action(self, action: ActionType):
        self.__chosen_action = action

    @held_item.setter
    def held_item(self, item: Item):
        self.__held_item = item

    @score.setter
    def score(self, score: int):
        self.__score = score

    @position.setter
    def score(self, position: tuple):
        self.__position = position

    def to_json(self):
        data = super().to_json()
        data['chosen_action'] = self.chosen_action
        data['held_item'] = self.held_item.to_json() if self.held_item is not None else None
        data['score'] = self.score
        return data

    def from_json(self, data: dict) -> 'Cook':
        super().from_json(data)
        self.chosen_action = data['chosen_action']
        self.score = data['score']
        temp: Item = data['held_item']
        if temp is None:
            self.held_item = None
        elif temp.object_type == ObjectType.pizza:
            self.held_item = Pizza().from_json(data['held_item'])
        else:
            self.held_item = Topping().from_json(data['held_item'])
        return self
