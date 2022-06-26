from xmlrpc.client import Boolean
from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item

import abc
class Station(GameObject):
    __metaclass__ = abc.ABCMeta
    



    def __init__(self, item: Item, is_infested : Boolean):
        super().__init__()
        self.object_type = ObjectType.station
        self.item: Item = item
        self.is_infested: Boolean = is_infested

    @property
    def item(self) -> GameObject:
        return self.__item

    @property
    def is_infested(self) -> Boolean:
        return self.__is_infested
    
    @item.setter
    def item(self, item: GameObject):
        self.__item = item

    @is_infested.setter
    def is_infested(self, bool: Boolean):
        self.__is_infested = bool


    @abc.abstractmethod
    def take_action(self):
        return

    

    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['item'] = self.item
        dict_data['is_infested'] = self.is_infested
        return dict_data

    def from_json(self, data: dict) -> 'Station':
        super().from_json(data)
        self.item = data['item']
        self.is_infested = data['is_infested']

    