from game.common.stations.station import Station
from game.common.enums import ObjectType, ToppingType
from game.common.items.item import Item
from game.common.items.topping import Topping


class Cutter(Station):
    def __init__(self, item: Item = None):
        super().__init__(item)
        self.object_type = ObjectType.cutter

    def take_action(self, item: Item) -> Item:
        if not isinstance(item, Topping) \
                or item.topping_type == ToppingType.dough:
            return item
        item.is_cut = True
        return item

    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Cutter':
        super().from_json(data)
        return self
