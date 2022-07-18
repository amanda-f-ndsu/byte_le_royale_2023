from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.enums import ObjectType
from game.common.stations.station import Station
from game.common.stats import GameStats

class Delivery(Station):
    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type = ObjectType.station #Does this need to be delivery?
        self.stored_pizza:Pizza = None

    @property
    def stored_pizza(self) -> Pizza:
        return self.__stored_pizza

    @stored_pizza.setter
    def stored_pizza(self, stored_pizza: Pizza):
        self.__stored_pizza = stored_pizza

    

    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Delivery':
        super().from_json(data)