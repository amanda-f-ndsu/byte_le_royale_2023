from xmlrpc.client import Boolean
from game.common.game_object import GameObject
from game.common.enums import ObjectType

class Station(GameObject):

    def __init__(self):
        super().__init__()
        self.object_type = ObjectType.station
        self.item: GameObject = None
        self.is_infested: Boolean = False

    @property
    def item(self) -> GameObject:
        return self.item

    @property
    def is_infested(self) -> Boolean:
        return self.is_infested
    
    @property.setter
    def item(self, item: GameObject):
        self.item = item

    @property.setter
    def is_infested(self, bool: Boolean):
        self.is_infested = bool


    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['item'] = self.item
        dict_data['is_infested'] = self.is_infested
        return dict_data

    def from_json(self, data: dict) -> 'Station':
        super().from_json(data)
        self.item = data['item']
        self.is_infested = data['is_infested']

    