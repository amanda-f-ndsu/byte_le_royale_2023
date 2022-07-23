from game.common.cook import Cook
from game.common.map.counter import Counter
from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.common.stations.station import Station


class Tile(GameObject):

    def __init__(self, occupied_by: GameObject = None, is_wet_tile=False):
        super().__init__()
        self.object_type = ObjectType.tile
        self.is_wet_tile = is_wet_tile
        # only a station, dispenser, or cook can occupy a tile. 'None' means tile is empty.
        self.occupied_by = occupied_by

    @property
    def is_wet_tile(self) -> bool:
        return self.__is_wet_tile

    @is_wet_tile.setter
    def is_wet_tile(self, is_wet_tile: bool):
        self.__is_wet_tile = is_wet_tile

    @property
    def occupied_by(self) -> GameObject:
        return self.__occupied_by

    @occupied_by.setter
    def occupied_by(self, occupied_by: GameObject):
        self.__occupied_by = occupied_by if occupied_by is None or isinstance(occupied_by, (Station, Counter, Cook)) else None

    def to_json(self):
        data = super().to_json()
        data['occupied_by'] = self.occupied_by
        data['is_wet_tile'] = self.is_wet_tile
        return data

    def from_json(self, data: dict) -> 'Tile':
        super().from_json(data)
        self.occupied_by = data['occupied_by']
        self.is_wet_tile = data['is_wet_tile']
        return self