import random

from game.common.stations.dispenser import Dispenser
from game.common.cook import Cook
from game.common.stations.bin import Bin
from game.common.stations.combiner import Combiner
from game.common.stations.oven import Oven
from game.common.stations.cutter import Cutter
from game.common.stations.roller import Roller
from game.common.stations.Sauce import Sauce
from game.common.stations.storage import Storage
from game.common.game_object import GameObject
from game.common.map.tile import Tile
from game.common.map.counter import Counter
from game.common.enums import ObjectType


class GameBoard(GameObject):
    def __init__(self, seed: int = None):
        random.seed(seed)
        super().__init__()
        self.object_type = ObjectType.game_board
        # generate list of stations
        station_hold = [
            Combiner(),
            Oven(),
            Oven(),
            Cutter(),
            Roller(),
            Sauce()
        ]

        # generate map
        self.game_map = [[Tile() for x in range(13)] for y in range(7)]
        # populate map
        temp_hold = []
        while len(station_hold) > 0:
            station_hold_len = len(station_hold)
            temp_hold.append(station_hold.pop(random.randint(0, station_hold_len)))

        temp_pop_data = [
            [
                Counter(),
                Counter(),
                temp_hold[0],
                temp_hold[1],
                temp_hold[2],
                Counter(),
                Counter(),
                Counter(),
                temp_hold[2],
                temp_hold[1],
                temp_hold[0],
                Counter(),
                Counter()
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Bin(),
                None,
                None,
                Cook(position = (3,3)),
                None,
                None,
                GameObject(),
                None,
                None,
                Cook(position = (3,9)),
                None,
                None,
                Bin(),
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Storage(),
                None,
                None,
                None,
                None,
                None,
                Dispenser(),
                None,
                None,
                None,
                None,
                None,
                Storage(),
            ],
            [
                Counter(),
                Counter(),
                temp_hold[3],
                temp_hold[4],
                temp_hold[5],
                Counter(),
                Counter(),
                Counter(),
                temp_hold[5],
                temp_hold[4],
                temp_hold[3],
                Counter(),
                Counter()
            ]
        ]
        for y in range(7):
            for x in range(13):
                if isinstance(self.game_map[y][x], Tile):
                    self.game_map[y][x].occupied_by = temp_pop_data[y][x]

    def ovens(self):
        to_return: list = list()
        to_return.extend(i.occupied_by for i in self.game_map[0] if isinstance(i.occupied_by, Oven))
        to_return.extend(i.occupied_by for i in self.game_map[len(self.game_map)-1] if isinstance(i.occupied_by, Oven))
        return to_return
    
    def cooks(self):
        to_return: list = list()
        to_return.append(self.game_map[3][3].occupied_by)
        to_return.append(self.game_map[3][9].occupied_by)
        return to_return

    def to_json(self):
        data = super(self).to_json()
        temp = map(lambda tile: tile.to_json(), self.game_map)
        data["game_map"] = temp

    def from_json(self, data):
        super().from_json(data)
        temp = data["game_map"]
        self.game_map = map(lambda tile: Tile().from_json(tile), temp)
