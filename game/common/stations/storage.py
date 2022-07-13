from xmlrpc.client import Boolean
from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item
import abc
class Storage(Station):
 

    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type = ObjectType.storage
        
    


    def take_action(self, item: Item):
        # if cook has pizza that has at least one topping, will be stored in oven
        item_rtn = item
       

        return item_rtn


    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Storage':
        super().from_json(data)
       
 