from xmlrpc.client import Boolean
from game.common.enums import ObjectType
from game.common.enums import *
from game.common.items.item import Item
from game.common.enums import ObjectType
from game.common.stations.station import Station

class Storage(Station):

    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type = ObjectType.storage


    def take_action(self, item: Item):
        # if cook is calling this method with an item parameter
        # this checks to make sure that there is nothing in the storage already
        
        if self.item != None:
            item_rtn = self.item
        
        self.item = item
            

        return item_rtn

    def take_action(self):
        #overload method that takes item if the cook doesn't have anyhting in hand
        item_rtn = self.item
        self.item == None
        return item_rtn


    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Storage':
        super().from_json(data)
       
 