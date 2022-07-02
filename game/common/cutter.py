from game.common.station import Station
from game.common.enums import ObjectType, ToppingType
from game.common.items.item import Item
from game.common.items.topping import Topping


class Cutter(Station):
    def __init__(self, item: Item = Item.empty()):
        super().__init__(item)
        self.object_type = ObjectType.roller

    def take_action(self, item_to_modify: Item) -> Item:
        if not isinstance(item_to_modify, Topping) \
                or item_to_modify.topping_type == ToppingType.dough:
            return item_to_modify
        item_to_modify.is_cut = True
        return item_to_modify

    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Cutter':
        super().from_json(data)
        return self
