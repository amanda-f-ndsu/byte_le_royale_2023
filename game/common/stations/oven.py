from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.enums import ObjectType
from game.common.stations.station import Station
from game.common.cook import Cook


class Oven(Station):
 

    def __init__(self, is_powered : bool = True):
        super().__init__()
        self.object_type = ObjectType.oven
        self.is_powered = is_powered
        
    @property
    def is_powered(self) -> bool:
        return self.__is_powered

    @is_powered.setter
    def is_powered(self, is_powered: bool):
        self.__is_powered = is_powered

    def take_action(self, cook: Cook):
        # if cook has pizza that has at least one topping, will be stored in oven
        if cook.held_item is not None and isinstance(cook.held_item,Pizza) and cook.held_item.state == PizzaState.sauced and (len(cook.held_item.toppings) >= 1):
            self.item = cook.held_item
            cook.held_item = None

        if cook.held_item is None and self.item is not None and (self.item.state == PizzaState.baked):
            cook.held_item = self.item
            self.item = None


    def to_json(self) -> dict:
        data = super().to_json()
        data['is_powered'] = self.is_powered
        return data

    def from_json(self, data: dict) -> 'Oven':
        super().from_json(data)
        self.is_powered = data['is_powered']
  

    