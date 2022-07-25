from game.common.cook import Cook
from game.common.stations.station import Station
from game.common.enums import ObjectType, PizzaState
from game.common.items.item import Item
from game.common.items.topping import Topping
from game.common.items.pizza import Pizza


class Combiner(Station):
    def __init__(self):
        super().__init__(None)
        self.object_type: ObjectType = ObjectType.combiner
        self.item = None

    def take_action(self, cook: Cook = None):
        # Check if a pizza is stored in station
        temp: Item = cook.held_item
        if not self.item:
            # Check if the item passed is a sauced pizza
            if isinstance(temp, Pizza) and temp.state == PizzaState.sauced:
                self.item = cook.held_item
                cook.held_item = None
            return None
        # If no item is being passed, return the stored pizza and set stored pizza to None
        if temp:
            pizza = self.item
            self.item = None
            return pizza
        # Check if item is topping
        if isinstance(temp, Topping) and temp.is_cut:
            return self.item.add_topping(cook.held_item)

    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Combiner':
        super().from_json(data)
        return self
