import random
import unittest
from game.controllers.wet_tiles_controller import WetTilesController
from game.utils.generate_game import generate_map
from game.common.cook import Cook
from game.common.game_board import GameBoard


class TestWetTilesController(unittest.TestCase):

    def setUp(self) -> None:
        self.WTC = WetTilesController()
        self.game_board = generate_map(1)
        self.off_board_cooks = [Cook(position=(0, 0)), Cook(position=(12, 0))]
        self.cooks = []
        for x in range(1, 6):
            for y in range(1, 6):
                self.cooks.append(Cook(position=(x, y)))

    # Generates wet-tile map without any cooks on it
    def test_create_wet_no_cook(self):
        self.WTC.handle_actions(self.game_board, self.off_board_cooks)
        self.determine_left_right_equality(self.game_board)

    # Test cooks at all tiles
    def test_wet_all_tile_cooks(self):
        while len(self.cooks) >= 2:
            two_cooks = [self.cooks.pop(random.randint(0, len(self.cooks) - 1)),
                         self.cooks.pop(random.randint(0, len(self.cooks) - 1))]
            self.WTC.handle_actions(self.game_board, two_cooks)
            self.determine_left_right_equality(self.game_board)

    # Possible wet-tile configurations generation on controller instantiation
    # Well less than 30 possible configuration, make sure no errors happen when none to choose
    def test_no_more_boards(self):
        two_cooks = [self.cooks.pop(random.randint(0, len(self.cooks) - 1)),
                     self.cooks.pop(random.randint(0, len(self.cooks) - 1))]
        for i in range(30):
            self.WTC.handle_actions(self.game_board, two_cooks)
            self.determine_left_right_equality(self.game_board)

    def determine_left_right_equality(self, game_map):
        self.left_map = {}
        # Get wet tiles on left hand map
        for x in range(6):
            for y in range(7):
                if self.game_board.game_map[y][x].is_wet_tile:
                    self.left_map[(y, x)] = self.game_board.game_map[y][x]
        self.right_map = {}
        # Get wet tiles on right hand map
        for x in range(7, 12):
            for y in range(7):
                if self.game_board.game_map[y][x].is_wet_tile:
                    self.right_map[(y, x)] = self.game_board.game_map[y][x]
        # Should have at least 1 wet tile on each side
        self.assertTrue(len(self.left_map) >= 1)
        self.assertTrue(len(self.right_map) >= 1)
        # Amount of wet tile should be same on both sides
        self.assertEqual(len(self.left_map), len(self.right_map))
        # Positions should be the same
        right_map_tile_pos = [(6 - (tile_pos[1] - 6), tile_pos[0]) for tile_pos in self.right_map.keys()]
        left_map_tile_pos = [(tile_pos[1], tile_pos[0]) for tile_pos in self.left_map.keys()]
        self.assertEqual(right_map_tile_pos, left_map_tile_pos)


if __name__ == '__main__':
    unittest.main()
