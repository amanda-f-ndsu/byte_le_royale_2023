from game.common.enums import *


class GameStats:
    topping_stats = {
        ToppingType.none: {'score': 0},
        # Dough score used as base pizza score
        ToppingType.dough: {'score': 50},
        ToppingType.cheese: {'score': 20},
        ToppingType.pepperoni: {'score': 40},
        ToppingType.sausage: {'score': 40},
        ToppingType.canadian_ham: {'score': 40},
        ToppingType.mushrooms: {'score': 40},
        ToppingType.peppers: {'score': 50},
        ToppingType.chicken: {'score': 40},
        ToppingType.olives: {'score': 50},
        ToppingType.anchovies: {'score': 50}
    }

    oven_timer = {
        'start': 50,
        'baked': 20
    }

    decay_rate = 0.02
    infested_decay_rate = 0.05
    event_timer = 50

