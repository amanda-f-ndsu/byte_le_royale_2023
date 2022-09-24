import unittest
from game.controllers.wet_tiles_controller import WetTilesController
from game.common.cook import Cook


class TestWetTilesController(unittest.TestCase):

    def setUp(self) -> None:
        self.WTC = WetTilesController()
        self.cooks = [
            Cook(position=(0, 0))
        ]

    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
