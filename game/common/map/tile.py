from game.common.cook import Cook
from game.common.map.counter import Counter
from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.common.stations.station import Station
from game.common.stations.bin import Bin
from game.common.stations.combiner import Combiner
from game.common.stations.cutter import Cutter
from game.common.stations.delivery import Delivery
from game.common.stations.dispenser import Dispenser
from game.common.stations.oven import Oven
from game.common.stations.roller import Roller
from game.common.stations.Sauce import Sauce
from game.common.stations.storage import Storage


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
        occupied_by = data['occupied_by']
        if not occupied_by:
            self.occupied_by = data['occupied_by']
        else:
            match occupied_by["object_type"]:
                case ObjectType.bin:
                    self.occupied_by = Bin().from_json(occupied_by)
                case ObjectType.combiner:
                    self.occupied_by = Combiner().from_json(occupied_by)
                case ObjectType.cutter:
                    self.occupied_by = Cutter().from_json(occupied_by)
                case ObjectType.delivery:
                    self.occupied_by = Delivery().from_json(occupied_by)
                case ObjectType.dispenser:
                    self.occupied_by = Dispenser().from_json(occupied_by)
                case ObjectType.oven:
                    self.occupied_by = Oven().from_json(occupied_by)
                case ObjectType.roller:
                    self.occupied_by = Roller().from_json(occupied_by)
                case ObjectType.sauce:
                    self.occupied_by = Sauce().from_json(occupied_by)
                case ObjectType.storage:
                    self.occupied_by = Storage().from_json(occupied_by)
                case ObjectType.counter:
                    self.occupied_by = Counter()
                case ObjectType.cook:
                    self.occupied_by = Cook().from_json(data['occupied_by'])
                case _:
                    raise Exception("Could not parse occupied_by")                  
        return self
