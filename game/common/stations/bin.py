from abc import ABC

from game.common.enums import *
from game.common.stations.station import Station


class Bin(Station, ABC):

    def __init__(self, cooldown: int = 0):
        super().__init__(None, None)
        self.cooldown = cooldown
        self.object_type = ObjectType.bin

    @property
    def cooldown(self) -> int:
        return self.__cooldown

    @cooldown.setter
    def cooldown(self, new_cooldown:int):
        self.__cooldown = new_cooldown

    def take_action(self):
        pass

    def to_json(self):
        data = super().to_json()
        data['cooldown'] = self.cooldown

    def from_json(self, data: dict) -> 'Bin':
        super().from_json(data)
        self.cooldown = data['cooldown']
        return self
