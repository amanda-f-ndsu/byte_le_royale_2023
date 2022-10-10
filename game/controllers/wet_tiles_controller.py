import random
from game.utils.generate_game import generate_map
from typing import List
from game.controllers.controller import Controller
from game.common.game_board import GameBoard
from game.common.cook import Cook


class WetTilesController(Controller):

    def __init__(self):
        super().__init__()
        self.wet_options = self.create_wet_options()

    # Assumed cook[0] is left cook[1] is right side of board
    def handle_actions(self, game_board, cooks):
        cook1_pos = cooks[0].position
        cook2_pos = cooks[1].position
        # Find distance to middle, then subtract that from middle to get position
        # the cook on right side would be on the left. In other words, reflection.
        cook2_superimposed = (6 - (cook2_pos[0] - 6), cook2_pos[1])

        cook1_calc_pos = cook1_pos[0] + cook1_pos[1] * 10
        cook2_calc_pos = cook2_superimposed[0] + cook2_superimposed[1] * 10

        chosen_board = False
        while not chosen_board and len(self.wet_options) != 0:
            trial_map = self.wet_options.pop(random.randint(0, len(self.wet_options) - 1))
            chosen_board = self.determine_game_board(trial_map, cook1_calc_pos, cook2_calc_pos)

        # Case no wet_tile map was chosen, don't do anything.
        if not chosen_board and len(self.wet_options) == 0:
            return

        # Update current game board to have wet tiles
        for y in range(7):
            for x in range(13):
                if chosen_board.game_map[y][x].is_wet_tile:
                    game_board.game_map[y][x].is_wet_tile = True


    def determine_game_board(self, trial_map: GameBoard, cook1_calc_pos: int, cook2_calc_pos: int):
        for y in range(7):
            for x in range(1, 6):
                tile_calc_pos = x + (y * 10)
                if trial_map.game_map[y][x].is_wet_tile and tile_calc_pos == cook1_calc_pos or tile_calc_pos == cook2_calc_pos:
                    # Player standing on wet_tile already, cannot use map
                    return False
        return trial_map


    def create_wet_options(self):
        wet_option_list = []

        four_corners = generate_map(5)
        four_corners.game_map[1][1].is_wet_tile = True
        four_corners.game_map[1][5].is_wet_tile = True
        four_corners.game_map[5][1].is_wet_tile = True
        four_corners.game_map[5][5].is_wet_tile = True

        four_corners.game_map[1][11].is_wet_tile = True
        four_corners.game_map[1][7].is_wet_tile = True
        four_corners.game_map[5][11].is_wet_tile = True
        four_corners.game_map[5][7].is_wet_tile = True
        wet_option_list.append(four_corners)

        rotting = generate_map(1)
        rotting.game_map[2][2].is_wet_tile = True
        rotting.game_map[3][1].is_wet_tile = True
        rotting.game_map[4][2].is_wet_tile = True

        rotting.game_map[2][10].is_wet_tile = True
        rotting.game_map[3][11].is_wet_tile = True
        rotting.game_map[4][10].is_wet_tile = True
        wet_option_list.append(rotting)

        starvation = generate_map(1)
        starvation.game_map[2][5].is_wet_tile = True
        starvation.game_map[4][5].is_wet_tile = True

        starvation.game_map[2][7].is_wet_tile = True
        starvation.game_map[4][7].is_wet_tile = True
        wet_option_list.append(starvation)

        bear_market = generate_map(1)
        bear_market.game_map[1][1].is_wet_tile = True
        bear_market.game_map[2][1].is_wet_tile = True
        bear_market.game_map[4][1].is_wet_tile = True
        bear_market.game_map[5][1].is_wet_tile = True

        bear_market.game_map[1][11].is_wet_tile = True
        bear_market.game_map[2][11].is_wet_tile = True
        bear_market.game_map[4][11].is_wet_tile = True
        bear_market.game_map[5][11].is_wet_tile = True
        wet_option_list.append(bear_market)

        smart_choices = generate_map(1)
        smart_choices.game_map[3][1].is_wet_tile = True

        smart_choices.game_map[3][11].is_wet_tile = True
        wet_option_list.append(smart_choices)

        ring_of_fire = generate_map(1)
        ring_of_fire.game_map[2][2].is_wet_tile = True
        ring_of_fire.game_map[2][3].is_wet_tile = True
        ring_of_fire.game_map[2][4].is_wet_tile = True
        ring_of_fire.game_map[3][2].is_wet_tile = True
        ring_of_fire.game_map[3][3].is_wet_tile = True
        ring_of_fire.game_map[3][4].is_wet_tile = True
        ring_of_fire.game_map[4][2].is_wet_tile = True
        ring_of_fire.game_map[4][3].is_wet_tile = True
        ring_of_fire.game_map[4][4].is_wet_tile = True

        ring_of_fire.game_map[2][10].is_wet_tile = True
        ring_of_fire.game_map[2][9].is_wet_tile = True
        ring_of_fire.game_map[2][8].is_wet_tile = True
        ring_of_fire.game_map[3][10].is_wet_tile = True
        ring_of_fire.game_map[3][9].is_wet_tile = True
        ring_of_fire.game_map[3][8].is_wet_tile = True
        ring_of_fire.game_map[4][10].is_wet_tile = True
        ring_of_fire.game_map[4][9].is_wet_tile = True
        ring_of_fire.game_map[4][8].is_wet_tile = True
        wet_option_list.append(ring_of_fire)

        no_oven = generate_map(1)
        no_oven.game_map[5][3].is_wet_tile = True

        no_oven.game_map[5][9].is_wet_tile = True
        wet_option_list.append(no_oven)

        pillar = generate_map(1)
        pillar.game_map[3][3].is_wet_tile = True

        pillar.game_map[3][9].is_wet_tile = True
        wet_option_list.append(pillar)

        return wet_option_list



