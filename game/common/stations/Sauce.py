from game.common.stations.station import Station
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza

class Sauce(Station):

    def __init__(self, item: Item = None):
        super().__init__(item)
        self.object_type = ObjectType.sauce

    def take_action(self, item: Item) -> Item:
        if item and isinstance(item, Pizza) and (item.state == PizzaState.rolled):
            item.state =PizzaState.sauced
            return item
        return item


    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Sauce':
        super().from_json(data)
        return self

