from game.common.enums import *
import math

class GameStats:
    topping_stats = {
        ToppingType.none: { 'score': 0 },
<<<<<<< HEAD

=======
>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
        #Dough score used as base pizza score
        ToppingType.dough: { 'score': 50 },
        ToppingType.cheese: { 'score': 20 },
        ToppingType.pepperoni: { 'score': 40 },
        ToppingType.sausage: { 'score': 40 },
        ToppingType.canadian_ham: { 'score': 40},
        ToppingType.mushrooms: { 'score' : 40},
        ToppingType.peppers: { 'score' : 50},
        ToppingType.chicken: { 'score' : 40},
        ToppingType.olives: { 'score' : 50},
        ToppingType.anchovies: { 'score' : 50}
<<<<<<< HEAD

=======
>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
    }

    oven_timer = {
        'start': 50,
        'baked': 20
<<<<<<< HEAD

=======
>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
    }