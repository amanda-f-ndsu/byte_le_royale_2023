from game.common.station import Station
from game.common.enums import ObjectType, ToppingType
from game.common.items.item import Item
from game.common.items.topping import Topping
from game.common.items.pizza import Pizza
from game.utils.helpers import cast


class Roller(Station):
    def __init__(self, item: Item = Item.empty()):
        super().__init__(item)
        self.object_type = ObjectType.roller

    def take_action(self, item_to_modify: Topping):
        # Return item if not a Topping
        if item_to_modify.object_type != ObjectType.topping:
            return item_to_modify
        # Downcast to topping
        # temp: Topping = Topping()
        # cast(item_to_modify, temp)
        # Return item if dough
        if item_to_modify.topping_type != ToppingType.dough:
            return item_to_modify
        # Return Pizza
        return Pizza()

    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Roller':
        super().from_json(data)
        return self
