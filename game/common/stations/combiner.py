from game.common.cook import Cook
from game.common.stations.station import Station
from game.common.enums import *
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
                return None
            return temp
        # If no item is being passed, return the stored pizza and set stored pizza to None
        if not temp:
            pizza = self.item
            self.item = None
            return pizza
        # Check if item is topping
        if isinstance(temp, Topping) and temp.is_cut:
            return self.item.add_topping(cook.held_item)

    def to_json(self) -> dict:
        dict_data = super().to_json()
<<<<<<< HEAD
        dict_data['stored_pizza'] = self.stored_pizza if self.stored_pizza is not None else None
=======
>>>>>>> 9cbfe081025a86333c828c00a063636586a2171a
        return dict_data

    def from_json(self, data: dict) -> 'Combiner':
        super().from_json(data)
<<<<<<< HEAD
        self.stored_pizza = data['stored_pizza'] if self.stored_pizza is not None else None

        return self
=======
        return self

>>>>>>> 9cbfe081025a86333c828c00a063636586a2171a
