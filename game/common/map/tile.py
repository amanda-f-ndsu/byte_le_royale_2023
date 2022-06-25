from game.common.cook import Cook
from game.common.dispenser import Dispenser
from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.common.station import Station


class Tile(GameObject):

    def __init__(self, occupied_by: GameObject=None):
        super().__init__()
        self.object_type = ObjectType.tile
        # only a station, dispenser, or cook can occupy a tile. 'None' means tile is empty.
        self.occupied_by = occupied_by 



    @property
    def occupied_by(self) -> GameObject:
        return self.__occupied_by

    @occupied_by.setter
    def occupied_by(self, occupied_by: GameObject):
        self.__occupied_by = occupied_by if occupied_by is None or isinstance(occupied_by, (Station, Dispenser, Cook)) else None


    def to_json(self):
        data = super().to_json()
        data['occupied_by'] = self.occupied_by
        return data

    def from_json(self, data: dict) -> 'Tile':
        super().from_json(data)
        self.occupied_by = data['occupied_by']
        return self