from xmlrpc.client import Boolean
from game.common.enums import ObjectType
from game.common.enums import *
from game.common.items.item import Item
from game.common.enums import ObjectType
from game.common.stations.station import Station
from typing import overload
class Storage(Station):

    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type = ObjectType.storage


    def take_action(self, item=None):
        # sets the item_rtn as the item in storage and if an item is passed in to the method, the item is stored.
        
        item_rtn = self.item
        self.item = None
        if isinstance(item, Item):
            self.item = item
        
        return item_rtn

  

    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Storage':
        super().from_json(data)
       
 