from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item
import abc

class Station(GameObject, metaclass=abc.ABCMeta):

    def __init__(self, item: Item = None, is_infested : bool = False):
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


    @abc.abstractmethod
    def take_action(self, item: Item = None):
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
        return self
