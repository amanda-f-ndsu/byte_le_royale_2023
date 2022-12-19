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
        # only a station, counter, or cook can occupy a tile. 'None' means tile is empty.
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
        if isinstance(occupied_by, (Station, Counter, Cook)):
            self.__occupied_by = occupied_by  
        else:
            self.__occupied_by = None 

    def to_json(self):
        data = super().to_json()
        data['occupied_by'] = self.occupied_by.to_json() if self.occupied_by else None
        data['is_wet_tile'] = self.is_wet_tile
        return data

    def from_json(self, data: dict) -> 'Tile':
        super().from_json(data)
        self.is_wet_tile = data['is_wet_tile']
        if not data['occupied_by']:
            self.occupied_by = data['occupied_by']
        elif data['occupied_by']["object_type"] in [ObjectType.bin, ObjectType.combiner, ObjectType.cutter, ObjectType.delivery, ObjectType.dispenser, ObjectType.oven, ObjectType.roller, ObjectType.sauce, ObjectType.storage]:
            station = Station()
            self.occupied_by = station.from_json(data['occupied_by'])
        elif data['occupied_by']["object_type"] == ObjectType.cook:
            breakpoint()
            self.occupied_by = Cook().from_json(data['occupied_by'])
        return self
