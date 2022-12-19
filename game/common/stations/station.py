from game.common.cook import Cook
from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from abc import abstractmethod, ABCMeta
from game.common.stations.bin import Bin
from game.common.stations.combiner import Combiner
from game.common.stations.cutter import Cutter
from game.common.stations.delivery import Delivery
from game.common.stations.dispenser import Dispenser
from game.common.stations.oven import Oven
from game.common.stations.roller import Roller
from game.common.stations.Sauce import Sauce
from game.common.stations.storage import Storage


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

    @abstractmethod
    def take_action(self, cook: Cook = None):
        return

    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['is_infested'] = self.is_infested
        dict_data['item'] = self.item.to_json() if self.item else None

        return dict_data

    def from_json(data: dict) -> 'Station':
        super().from_json(data)
        sub_station_type = None
        if data["object_type"] == ObjectType.bin:
            sub_station_type = Bin()
        elif data["object_type"] == ObjectType.combiner:
            sub_station_type = Combiner()
        if sub_station_type:
            sub_station_type = data['is_infested']
            if not data['item']:
                sub_station_type.item = None
            if data['item'].object_type == ObjectType.pizza:
                sub_station_type.item = Pizza().from_json(data['item'])
            elif data['item'].object_type == ObjectType.topping:
                sub_station_type.item = Topping().from_json(data['item'])

            return sub_station_type
