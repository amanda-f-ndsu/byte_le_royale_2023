from game.common.enums import *
import math

class GameStats:
    topping_stats = {
        ToppingType.none: { 'score': 0 },
        ToppingType.dough: { 'score': 0 },
        ToppingType.cheese: { 'score': 20 },
        ToppingType.pepperoni: { 'score': 40 },
        ToppingType.sausage: { 'score': 40 },
        ToppingType.canadian_ham: { 'score': 40},
        ToppingType.mushrooms: { 'score' : 40},
        ToppingType.peppers: { 'score' : 50},
        ToppingType.chicken: { 'score' : 40},
        ToppingType.olives: { 'score' : 50},
        ToppingType.anchovies: { 'score' : 50}
    }

    oven_timer = {
        'start': 50,
        'baked': 20
    }

    map_stats = {
        'width' : 5,
        'height' : 5
    }