from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item
from abc import abstractmethod


class Station(GameObject):

    def __init__(self, item: Item = Item.empty(), is_infested: bool = False):
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
        self.__item = item

    @is_infested.setter
    def is_infested(self, infested: bool):
        self.__is_infested = infested

    @abstractmethod
    def take_action(self, item_to_modify: Item) -> Item:
        return item_to_modify

    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['item'] = self.item
        dict_data['is_infested'] = self.is_infested
        return dict_data

    def from_json(self, data: dict) -> 'Station':
        super().from_json(data)
        self.item = data['item']
        self.is_infested = data['is_infested']
        return self
