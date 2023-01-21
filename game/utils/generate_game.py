from game.config import *
from game.utils.helpers import write_json_file
from game.common.game_board import GameBoard
import random


def generate(seed: int = random.randint(0,1000000000)):
    print('Generating game map...')

    data = dict()

    # for x in range(1, MAX_TICKS + 1):
    #     data[x] = 'data'

    # Verify logs location exists
    if not os.path.exists(GAME_MAP_DIR):
        os.mkdir(GAME_MAP_DIR)

    data['game_map'] = generate_map(seed).to_json()
    data['seed'] = seed
    # Write game map to file
    write_json_file(data, GAME_MAP_FILE)


def generate_map(seed: int = None):
    return GameBoard(seed)

