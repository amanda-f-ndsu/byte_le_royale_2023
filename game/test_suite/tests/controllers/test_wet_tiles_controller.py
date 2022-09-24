import unittest
from game.controllers.wet_tiles_controller import WetTilesController
from game.utils.generate_game import generate_map
from game.common.cook import Cook
from game.common.game_board import GameBoard


class TestWetTilesController(unittest.TestCase):

    def setUp(self) -> None:
        self.WTC = WetTilesController()
        self.game_board = generate_map(1)
        self.off_board_cook = Cook(position=(0, 0))
        self.cooks = []
        for x in range(1, 6):
            for y in range(1, 6):
                self.cooks.append(Cook(position=(x, y)))

    def test_create_wet_no_cook(self):
        self.WTC.handle_actions(self.game_board, self.off_board_cook)
        for x in range(13):
            for y in range(7):
                self.assertFalse(self.game_board.game_map[y, x])


if __name__ == '__main__':
    unittest.main()
