from game.common.action import Action
from game.common.enums import ActionType, ObjectType
from game.common.game_object import GameObject
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping


class Cook(GameObject):
    def __init__(self, item: Item = None, position=None):
        super().__init__()
        self.object_type = ObjectType.cook
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
    # return format for tuple (x-position, y-position), assumes (0,0) is top left of the game board
    def position(self) -> tuple:
        return self.__position

    @held_item.setter
    def held_item(self, item: Item):
        if isinstance(item, Item) or item is None:
            self.__held_item = item

    @score.setter
    def score(self, score: int):
        self.__score = score

    @position.setter
    def position(self, position: tuple):
        self.__position = position

    def to_json(self):
        data = super().to_json()
        data['held_item'] = self.held_item.to_json() if self.held_item else None
        data['score'] = self.score
        data['position'] = self.position
        return data

    def from_json(self, data: dict) -> 'Cook':
        super().from_json(data)
        self.score = data['score']
        self.position = data['position']
        temp: Item = data['held_item']
        if temp is None:
            self.held_item = None
        elif temp.object_type == ObjectType.pizza:
            self.held_item = Pizza().from_json(data['held_item'])
        else:
            self.held_item = Topping().from_json(data['held_item'])
        return self
