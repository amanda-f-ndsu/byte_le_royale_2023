from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.enums import ObjectType
from game.common.stations.station import Station
from game.common.stats import GameStats


class Oven(Station):
    def __init__(self, item: Item = None,
                 is_infested: bool = False,
                 is_powered: bool = True,
                 is_active: bool = False,
                 timer: int = GameStats.oven_timer['start']):
        super().__init__(item, is_infested)
        self.object_type = ObjectType.oven
        self.is_powered = is_powered
        self.is_active = is_active
        self.timer = timer
        
    @property
    def is_powered(self) -> bool:
        return self.__is_powered

    @is_powered.setter
    def is_powered(self, is_powered: bool):
        self.__is_powered = is_powered

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        self.__is_active = is_active

    def take_action(self, cook: Cook = None):
        # if cook has pizza that has at least one topping, will be stored in oven
        item_rtn = cook.held_item
        if item_rtn and isinstance(item_rtn, Pizza) \
                and item_rtn.state == PizzaState.sauced \
                and (len(item_rtn.toppings) > 0):
            self.is_active = True
            self.item = cook.held_item
            item_rtn = None

        if not cook.held_item and self.item and (self.item.state == PizzaState.baked):
            item_rtn = self.item
            self.item = None
        return item_rtn

    def to_json(self) -> dict:
        data = super().to_json()
        data['is_powered'] = self.is_powered
        data['is_active'] = self.is_active
        data['timer'] = self.timer
        return data

    def from_json(self, data: dict) -> 'Oven':
        super().from_json(data)
        self.is_powered = data['is_powered']
        self.is_active = data['is_active']
        self.timer = data['timer']
        return self

    def power_outage(self):
        self.is_powered(self, False)

    def power_reset(self):
        self.is_powered(self, True)