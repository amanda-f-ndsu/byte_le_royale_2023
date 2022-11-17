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
from game.common.stations.delivery import Delivery


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
            temp_hold.append(station_hold.pop(random.randint(0, len(station_hold)-1)))

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
                Cook(position=(3, 3)),
                None,
                None,
                Delivery(),
                None,
                None,
                Cook(position=(9, 3)),
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

        # i = row index, y is row in 2d array
        for i, y in enumerate(temp_pop_data):
            # j = column index, x is item in 2d array
            # set item to game_map[y][x].occupied_by
            for j, x in enumerate(y):
                self.game_map[i][j].occupied_by = x

    def ovens(self):
        to_return: list = list()
        to_return.extend([i.occupied_by for i in self.game_map[0] if isinstance(i.occupied_by, Oven)])
        to_return.extend([i.occupied_by for i in self.game_map[len(self.game_map)-1] if isinstance(i.occupied_by, Oven)])
        return to_return
    
    def cooks(self):
        to_return: list = list(filter(lambda row: len(row) > 0, [[tile.occupied_by for tile in row if isinstance(tile.occupied_by, Cook)] for row in self.game_map]))
        return to_return[0] if len(to_return) == 1 else (to_return[0][0], to_return[1][0])

    def to_json(self):
        data = super().to_json()
        temp = list([list(map(lambda tile: tile.to_json(), y)) for y in self.game_map])
        data["game_map"] = temp
        return data

    def from_json(self, data):
        super().from_json(data)
        temp = data["game_map"]
        self.game_map = list([list(map(lambda tile: Tile().from_json(tile), y)) for y in temp])
        return self
