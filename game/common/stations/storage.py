from game.common.cook import Cook
from game.common.items.item import Item
from game.common.items.topping import Topping
from game.common.enums import ObjectType
from game.common.items.pizza import Pizza
from game.common.stations.station import Station


class Storage(Station):

    def __init__(self, item: Item = None, is_infested: bool = False):
        super().__init__(item, is_infested)
        self.object_type = ObjectType.storage


    def take_action(self, cook: Cook):
        # sets the item_rtn as the item in storage and if an item is passed in to the method, the item is stored.
        
        item_rtn = self.item
        self.item = None
        if isinstance(cook.held_item, Item):
            self.item = cook.held_item
        
        return item_rtn


    def to_json(self) -> dict:
        data = super().to_json()
        data['item'] = self.item.to_json() if self.item else None
        return data

    def from_json(self, data: dict) -> 'Storage':
        super().from_json(data)
        temp: Item = data['item']
        if not temp:
            self.item = None
        elif temp.object_type == ObjectType.pizza:
            self.item = Pizza().from_json(data['item'])
        else:
            self.item = Topping().from_json(data['item'])
        return self
