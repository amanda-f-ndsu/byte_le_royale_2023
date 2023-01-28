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
        cook2_superimposed = (cook2_pos[0], 6 - (cook2_pos[1] - 6))

        cook1_calc_pos = cook1_pos[1] + cook1_pos[0] * 10
        cook2_calc_pos = cook2_superimposed[1] + cook2_superimposed[0] * 10

        # Determine which of the wet_tile boards to choose
        chosen_board = False
        while not chosen_board and len(self.wet_options) != 0:
            trial_map = self.wet_options.pop(random.randint(0, len(self.wet_options) - 1))
            chosen_board = self.determine_game_board(trial_map, cook1_calc_pos, cook2_calc_pos)

        # Case no wet_tile map was chosen, don't do anything.
        if not chosen_board and len(self.wet_options) == 0:
            return False

        # Update current game board to have wet tiles
        for y in range(7):
            for x in range(13):
                if chosen_board.game_map[y][x].is_wet_tile:
                    game_board.game_map[y][x].is_wet_tile = True
        return True


    def determine_game_board(self, trial_map: GameBoard, cook1_calc_pos: int, cook2_calc_pos: int):
        for y in range(7):
            for x in range(1, 6):
                tile_calc_pos = x + (y * 10)
                if trial_map.game_map[y][x].is_wet_tile and (tile_calc_pos == cook1_calc_pos or tile_calc_pos == cook2_calc_pos):         
                    # Player standing on wet_tile already, cannot use map
                    return False
        return trial_map

    # Maps appended more than once in this method to improve odds of being chosen
    # Yes, I know this is a bad solution and non-performant
    # This is a night-before QOL change that get's the job done (game is running good and don't want to do anything error-prone/drastic)
    # For those reading this file in 2023+ for some reason, firstly, I am honored for you to have choose my file to look at.
    # Secondly, Mitchell Borders (wet_tiles_controller author) say's hello.
    def create_wet_options(self):
        wet_option_list = []

        rainbow = generate_map(1)
        rainbow.game_map[1][5].is_wet_tile = True
        rainbow.game_map[3][3].is_wet_tile = True
        rainbow.game_map[5][1].is_wet_tile = True
        rainbow.game_map[2][3].is_wet_tile = True
        rainbow.game_map[4][3].is_wet_tile = True

        rainbow.game_map[1][7].is_wet_tile = True
        rainbow.game_map[3][9].is_wet_tile = True
        rainbow.game_map[5][11].is_wet_tile = True
        rainbow.game_map[2][9].is_wet_tile = True
        rainbow.game_map[4][9].is_wet_tile = True
        wet_option_list.append(rainbow)
        wet_option_list.append(rainbow)

        waluigi = generate_map(1)
        waluigi.game_map[4][4].is_wet_tile = True
        waluigi.game_map[4][3].is_wet_tile = True
        waluigi.game_map[4][2].is_wet_tile = True
        waluigi.game_map[4][1].is_wet_tile = True
        waluigi.game_map[3][1].is_wet_tile = True
        waluigi.game_map[2][1].is_wet_tile = True

        waluigi.game_map[4][8].is_wet_tile = True
        waluigi.game_map[4][9].is_wet_tile = True
        waluigi.game_map[4][10].is_wet_tile = True
        waluigi.game_map[4][11].is_wet_tile = True
        waluigi.game_map[3][11].is_wet_tile = True
        waluigi.game_map[2][11].is_wet_tile = True
        wet_option_list.append(waluigi)
        wet_option_list.append(waluigi)

        luigi = generate_map(1)
        luigi.game_map[4][4].is_wet_tile = True
        luigi.game_map[4][3].is_wet_tile = True
        luigi.game_map[4][2].is_wet_tile = True
        luigi.game_map[4][1].is_wet_tile = True
        luigi.game_map[3][1].is_wet_tile = True
        luigi.game_map[2][1].is_wet_tile = True

        luigi.game_map[4][8].is_wet_tile = True
        luigi.game_map[4][9].is_wet_tile = True
        luigi.game_map[4][10].is_wet_tile = True
        luigi.game_map[4][11].is_wet_tile = True
        luigi.game_map[3][11].is_wet_tile = True
        luigi.game_map[2][11].is_wet_tile = True
        wet_option_list.append(luigi)
        wet_option_list.append(luigi)

        path = generate_map(1)
        path.game_map[1][1].is_wet_tile = True
        path.game_map[2][1].is_wet_tile = True
        path.game_map[3][1].is_wet_tile = True
        path.game_map[4][1].is_wet_tile = True
        path.game_map[5][1].is_wet_tile = True
        path.game_map[2][2].is_wet_tile = True
        path.game_map[3][2].is_wet_tile = True
        path.game_map[4][2].is_wet_tile = True
        path.game_map[2][3].is_wet_tile = True
        path.game_map[3][3].is_wet_tile = True
        path.game_map[4][3].is_wet_tile = True
        path.game_map[2][4].is_wet_tile = True
        path.game_map[3][4].is_wet_tile = True
        path.game_map[4][4].is_wet_tile = True

        path.game_map[1][11].is_wet_tile = True
        path.game_map[2][11].is_wet_tile = True
        path.game_map[3][11].is_wet_tile = True
        path.game_map[4][11].is_wet_tile = True
        path.game_map[5][11].is_wet_tile = True
        path.game_map[2][10].is_wet_tile = True
        path.game_map[3][10].is_wet_tile = True
        path.game_map[4][10].is_wet_tile = True
        path.game_map[2][9].is_wet_tile = True
        path.game_map[3][9].is_wet_tile = True
        path.game_map[4][9].is_wet_tile = True
        path.game_map[2][8].is_wet_tile = True
        path.game_map[3][8].is_wet_tile = True
        path.game_map[4][8].is_wet_tile = True
        wet_option_list.append(path)
        wet_option_list.append(path)

        line = generate_map(1)
        line.game_map[2][1].is_wet_tile = True
        line.game_map[3][1].is_wet_tile = True
        line.game_map[4][1].is_wet_tile = True
        line.game_map[2][2].is_wet_tile = True
        line.game_map[3][2].is_wet_tile = True
        line.game_map[4][2].is_wet_tile = True
        line.game_map[2][3].is_wet_tile = True
        line.game_map[4][3].is_wet_tile = True
        line.game_map[2][4].is_wet_tile = True
        line.game_map[4][4].is_wet_tile = True
        line.game_map[2][5].is_wet_tile = True
        line.game_map[4][5].is_wet_tile = True

        line.game_map[2][11].is_wet_tile = True
        line.game_map[3][11].is_wet_tile = True
        line.game_map[4][11].is_wet_tile = True
        line.game_map[2][10].is_wet_tile = True
        line.game_map[3][10].is_wet_tile = True
        line.game_map[4][10].is_wet_tile = True
        line.game_map[2][9].is_wet_tile = True
        line.game_map[4][9].is_wet_tile = True
        line.game_map[2][8].is_wet_tile = True
        line.game_map[4][8].is_wet_tile = True
        line.game_map[2][7].is_wet_tile = True
        line.game_map[4][7].is_wet_tile = True
        wet_option_list.append(line)
        wet_option_list.append(line)


        snake = generate_map(1)
        snake.game_map[4][1].is_wet_tile = True
        snake.game_map[2][2].is_wet_tile = True
        snake.game_map[4][2].is_wet_tile = True
        snake.game_map[2][3].is_wet_tile = True
        snake.game_map[4][3].is_wet_tile = True
        snake.game_map[2][4].is_wet_tile = True
        snake.game_map[4][4].is_wet_tile = True
        snake.game_map[2][5].is_wet_tile = True

        snake.game_map[4][11].is_wet_tile = True
        snake.game_map[2][10].is_wet_tile = True
        snake.game_map[4][10].is_wet_tile = True
        snake.game_map[2][9].is_wet_tile = True
        snake.game_map[4][9].is_wet_tile = True
        snake.game_map[2][8].is_wet_tile = True
        snake.game_map[4][8].is_wet_tile = True
        snake.game_map[2][7].is_wet_tile = True
        wet_option_list.append(snake)
        wet_option_list.append(snake)


        revsnake = generate_map(1)
        revsnake.game_map[2][1].is_wet_tile = True
        revsnake.game_map[2][2].is_wet_tile = True
        revsnake.game_map[4][2].is_wet_tile = True
        revsnake.game_map[2][3].is_wet_tile = True
        revsnake.game_map[4][3].is_wet_tile = True
        revsnake.game_map[2][4].is_wet_tile = True
        revsnake.game_map[4][4].is_wet_tile = True
        revsnake.game_map[4][5].is_wet_tile = True

        revsnake.game_map[2][11].is_wet_tile = True
        revsnake.game_map[2][10].is_wet_tile = True
        revsnake.game_map[4][10].is_wet_tile = True
        revsnake.game_map[2][9].is_wet_tile = True
        revsnake.game_map[4][9].is_wet_tile = True
        revsnake.game_map[2][8].is_wet_tile = True
        revsnake.game_map[4][8].is_wet_tile = True
        revsnake.game_map[4][7].is_wet_tile = True
        wet_option_list.append(revsnake)
        wet_option_list.append(revsnake)


        smsnake = generate_map(1)
        smsnake.game_map[4][1].is_wet_tile = True
        smsnake.game_map[3][1].is_wet_tile = True
        smsnake.game_map[2][1].is_wet_tile = True
        smsnake.game_map[4][2].is_wet_tile = True
        smsnake.game_map[2][3].is_wet_tile = True
        smsnake.game_map[4][3].is_wet_tile = True
        smsnake.game_map[2][4].is_wet_tile = True
        smsnake.game_map[2][5].is_wet_tile = True
        smsnake.game_map[4][5].is_wet_tile = True

        smsnake.game_map[4][11].is_wet_tile = True
        smsnake.game_map[3][11].is_wet_tile = True
        smsnake.game_map[2][11].is_wet_tile = True
        smsnake.game_map[4][10].is_wet_tile = True
        smsnake.game_map[2][9].is_wet_tile = True
        smsnake.game_map[4][9].is_wet_tile = True
        smsnake.game_map[2][8].is_wet_tile = True
        smsnake.game_map[2][7].is_wet_tile = True
        smsnake.game_map[4][7].is_wet_tile = True
        wet_option_list.append(smsnake)
        wet_option_list.append(smsnake)


        revsmsnake = generate_map(1)
        revsmsnake.game_map[4][1].is_wet_tile = True
        revsmsnake.game_map[3][1].is_wet_tile = True
        revsmsnake.game_map[2][1].is_wet_tile = True
        revsmsnake.game_map[2][2].is_wet_tile = True
        revsmsnake.game_map[2][3].is_wet_tile = True
        revsmsnake.game_map[4][3].is_wet_tile = True
        revsmsnake.game_map[4][4].is_wet_tile = True
        revsmsnake.game_map[2][5].is_wet_tile = True
        revsmsnake.game_map[4][5].is_wet_tile = True

        revsmsnake.game_map[4][11].is_wet_tile = True
        revsmsnake.game_map[3][11].is_wet_tile = True
        revsmsnake.game_map[2][11].is_wet_tile = True
        revsmsnake.game_map[2][10].is_wet_tile = True
        revsmsnake.game_map[2][9].is_wet_tile = True
        revsmsnake.game_map[4][9].is_wet_tile = True
        revsmsnake.game_map[4][8].is_wet_tile = True
        revsmsnake.game_map[2][7].is_wet_tile = True
        revsmsnake.game_map[4][7].is_wet_tile = True
        wet_option_list.append(revsmsnake)
        wet_option_list.append(revsmsnake)


        patha = generate_map(1)
        patha.game_map[2][1].is_wet_tile = True
        patha.game_map[3][1].is_wet_tile = True
        patha.game_map[4][1].is_wet_tile = True
        patha.game_map[2][2].is_wet_tile = True
        patha.game_map[3][2].is_wet_tile = True
        patha.game_map[4][2].is_wet_tile = True
        patha.game_map[2][3].is_wet_tile = True
        patha.game_map[3][3].is_wet_tile = True
        patha.game_map[4][3].is_wet_tile = True
        patha.game_map[2][4].is_wet_tile = True
        patha.game_map[3][4].is_wet_tile = True
        patha.game_map[4][4].is_wet_tile = True

        patha.game_map[2][11].is_wet_tile = True
        patha.game_map[3][11].is_wet_tile = True
        patha.game_map[4][11].is_wet_tile = True
        patha.game_map[2][10].is_wet_tile = True
        patha.game_map[3][10].is_wet_tile = True
        patha.game_map[4][10].is_wet_tile = True
        patha.game_map[2][9].is_wet_tile = True
        patha.game_map[3][9].is_wet_tile = True
        patha.game_map[4][9].is_wet_tile = True
        patha.game_map[2][8].is_wet_tile = True
        patha.game_map[3][8].is_wet_tile = True
        patha.game_map[4][8].is_wet_tile = True
        wet_option_list.append(patha)
        wet_option_list.append(patha)


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

        bear_market.game_map[1][11].is_wet_tile = True
        bear_market.game_map[2][11].is_wet_tile = True
        bear_market.game_map[4][11].is_wet_tile = True
        wet_option_list.append(bear_market)

        smart_choices = generate_map(1)
        smart_choices.game_map[3][1].is_wet_tile = True
        smart_choices.game_map[3][3].is_wet_tile = True
        smart_choices.game_map[3][4].is_wet_tile = True

        smart_choices.game_map[3][11].is_wet_tile = True
        smart_choices.game_map[3][9].is_wet_tile = True
        smart_choices.game_map[3][8].is_wet_tile = True
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
        wet_option_list.append(ring_of_fire)

        pillar = generate_map(1)
        pillar.game_map[3][3].is_wet_tile = True

        pillar.game_map[3][9].is_wet_tile = True
        wet_option_list.append(pillar)

        great_wall_vert = generate_map(1)
        great_wall_vert.game_map[3][1].is_wet_tile = True
        great_wall_vert.game_map[3][2].is_wet_tile = True
        great_wall_vert.game_map[3][3].is_wet_tile = True
        great_wall_vert.game_map[3][2].is_wet_tile = True
        great_wall_vert.game_map[4][3].is_wet_tile = True

        great_wall_vert.game_map[3][11].is_wet_tile = True
        great_wall_vert.game_map[3][10].is_wet_tile = True
        great_wall_vert.game_map[3][9].is_wet_tile = True
        great_wall_vert.game_map[3][10].is_wet_tile = True
        great_wall_vert.game_map[4][9].is_wet_tile = True
        wet_option_list.append(great_wall_vert)
        wet_option_list.append(great_wall_vert)

        great_wall_hor = generate_map(1)
        great_wall_hor.game_map[3][1].is_wet_tile = True
        great_wall_hor.game_map[3][2].is_wet_tile = True
        great_wall_hor.game_map[3][3].is_wet_tile = True
        great_wall_hor.game_map[3][4].is_wet_tile = True

        great_wall_hor.game_map[3][11].is_wet_tile = True
        great_wall_hor.game_map[3][10].is_wet_tile = True
        great_wall_hor.game_map[3][9].is_wet_tile = True
        great_wall_hor.game_map[3][8].is_wet_tile = True
        wet_option_list.append(great_wall_hor)
        wet_option_list.append(great_wall_hor)


        famine = generate_map(1)
        famine.game_map[2][5].is_wet_tile = True
        famine.game_map[4][5].is_wet_tile = True
        famine.game_map[5][5].is_wet_tile = True

        famine.game_map[2][7].is_wet_tile = True
        famine.game_map[4][7].is_wet_tile = True
        famine.game_map[5][7].is_wet_tile = True
        wet_option_list.append(famine)
        wet_option_list.append(famine)


        filter = generate_map(1)
        filter.game_map[3][2].is_wet_tile = True
        filter.game_map[3][4].is_wet_tile = True

        filter.game_map[3][10].is_wet_tile = True
        filter.game_map[3][8].is_wet_tile = True
        wet_option_list.append(filter)

        reset = generate_map(1)
        reset.game_map[2][2].is_wet_tile = True
        reset.game_map[2][3].is_wet_tile = True
        reset.game_map[2][4].is_wet_tile = True
        reset.game_map[4][2].is_wet_tile = True
        reset.game_map[4][3].is_wet_tile = True
        reset.game_map[4][4].is_wet_tile = True

        reset.game_map[2][10].is_wet_tile = True
        reset.game_map[2][9].is_wet_tile = True
        reset.game_map[2][8].is_wet_tile = True
        reset.game_map[4][10].is_wet_tile = True
        reset.game_map[4][9].is_wet_tile = True
        reset.game_map[4][8].is_wet_tile = True
        wet_option_list.append(reset)
        wet_option_list.append(reset)


        diagonal = generate_map(1)
        diagonal.game_map[2][4].is_wet_tile = True
        diagonal.game_map[4][2].is_wet_tile = True

        diagonal.game_map[2][8].is_wet_tile = True
        diagonal.game_map[4][10].is_wet_tile = True
        wet_option_list.append(diagonal)

        small_four_corners = generate_map()
        small_four_corners.game_map[2][2].is_wet_tile = True
        small_four_corners.game_map[2][4].is_wet_tile = True
        small_four_corners.game_map[4][2].is_wet_tile = True
        small_four_corners.game_map[4][4].is_wet_tile = True

        small_four_corners.game_map[2][10].is_wet_tile = True
        small_four_corners.game_map[2][8].is_wet_tile = True
        small_four_corners.game_map[4][10].is_wet_tile = True
        small_four_corners.game_map[4][8].is_wet_tile = True
        wet_option_list.append(small_four_corners)
        wet_option_list.append(small_four_corners)


        loco = generate_map(1)
        loco.game_map[5][1].is_wet_tile = True
        loco.game_map[2][2].is_wet_tile = True
        loco.game_map[2][4].is_wet_tile = True
        loco.game_map[4][3].is_wet_tile = True

        loco.game_map[5][11].is_wet_tile = True
        loco.game_map[2][10].is_wet_tile = True
        loco.game_map[2][8].is_wet_tile = True
        loco.game_map[4][9].is_wet_tile = True
        wet_option_list.append(loco)

        hut_hut = generate_map(1)
        hut_hut.game_map[2][4].is_wet_tile = True
        hut_hut.game_map[4][4].is_wet_tile = True

        hut_hut.game_map[2][8].is_wet_tile = True
        hut_hut.game_map[4][8].is_wet_tile = True
        wet_option_list.append(hut_hut)

        issa_L = generate_map(1)
        issa_L.game_map[2][2].is_wet_tile = True
        issa_L.game_map[4][2].is_wet_tile = True
        issa_L.game_map[4][5].is_wet_tile = True

        issa_L.game_map[2][10].is_wet_tile = True
        issa_L.game_map[4][10].is_wet_tile = True
        issa_L.game_map[4][7].is_wet_tile = True
        wet_option_list.append(issa_L)

        diag_filter = generate_map(1)
        diag_filter.game_map[4][1].is_wet_tile = True
        diag_filter.game_map[3][2].is_wet_tile = True
        diag_filter.game_map[2][3].is_wet_tile = True
        diag_filter.game_map[4][5].is_wet_tile = True

        diag_filter.game_map[4][11].is_wet_tile = True
        diag_filter.game_map[3][10].is_wet_tile = True
        diag_filter.game_map[2][9].is_wet_tile = True
        diag_filter.game_map[4][7].is_wet_tile = True
        wet_option_list.append(diag_filter)
        wet_option_list.append(diag_filter)


        return wet_option_list



