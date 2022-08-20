from abc import ABC
from game.common.cook import Cook
from game.common.enums import *
from game.common.stations.station import Station


class Bin(Station, ABC):
    def __init__(self):
        super().__init__(None, False)
        self.object_type = ObjectType.bin

    def take_action(self, cook: Cook = None):
        return None

    def to_json(self):
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Bin':
        super().from_json(data)
        return self
