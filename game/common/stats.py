from game.common.enums import *


class GameStats:
    topping_stats = {
        ToppingType.none: {'score': 0},
        # Dough score used as base pizza score
        ToppingType.dough: {'score': 50},
        ToppingType.cheese: {'score': 55},
        ToppingType.pepperoni: {'score': 65},
        ToppingType.sausage: {'score': 60},
        ToppingType.canadian_ham: {'score': 70},
        ToppingType.mushrooms: {'score': 70},
        ToppingType.peppers: {'score': 75},
        ToppingType.chicken: {'score': 60},
        ToppingType.olives: {'score': 65},
        ToppingType.anchovies: {'score': 100}
    }

    oven_timer = {
        'start': 50,
        'baked': 20
    }

    decay_rate = 0.005
    infested_decay_rate = 0.01
    event_timer = 50
    turns_per_item_turnover_event = 12

    topping_types_synced_list = [ToppingType.dough,
                                 ToppingType.cheese,
                                 ToppingType.pepperoni,
                                 ToppingType.sausage,
                                 ToppingType.canadian_ham,
                                 ToppingType.mushrooms,
                                 ToppingType.peppers,
                                 ToppingType.chicken,
                                 ToppingType.olives,
                                 ToppingType.anchovies]
    topping_types_weights_array = [
        .3, .24, .1, .1, .05, .03, .02, .1, .05, .01]
