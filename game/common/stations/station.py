from game.common.cook import Cook
from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping


class Station(GameObject):
    def __init__(self, item: Item = None, is_infested: bool = False):
        super().__init__()
        self.object_type = ObjectType.station
        self.item: Item = item
        self.is_infested: bool = is_infested

    @property
    def item(self) -> Item:
        return self.__item

    @property
    def is_infested(self) -> bool:
        return self.__is_infested

    @item.setter
    def item(self, item: Item):
        self.__item = item if isinstance(item, Item) else None

    @is_infested.setter
    def is_infested(self, is_infested: bool):
        self.__is_infested = is_infested

    def take_action(self, cook: Cook = None):
        return

    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['is_infested'] = self.is_infested
        dict_data['item'] = self.item.to_json() if self.item else None

        return dict_data

    def from_json(self, data: dict) -> 'Station':
        super().from_json(data)
        self.is_infested = data['is_infested']
        if not data['item']:
            self.item = None
        elif data['item']["object_type"] == ObjectType.pizza:
            self.item = Pizza().from_json(data['item'])
        elif data['item']["object_type"] == ObjectType.topping:
            self.item = Topping().from_json(data['item'])

        return self