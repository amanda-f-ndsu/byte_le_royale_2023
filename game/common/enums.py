from enum import Enum

<<<<<<< HEAD
=======

>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
class DebugLevel:
    none = 0
    client = 1
    controller = 2
    engine = 3


class ObjectType:
    none = 0
    action = 1
    player = 2
    item = 3
    dispenser = 4
    station = 5
    cook = 6
    topping = 7
    tile = 8
    pizza = 9
    roller = 10
    cutter = 11
    oven = 12
    bin = 13
    combiner = 14
    storage = 15
    delivery = 16
    sauce = 17

class ActionType:
    none = 0
    test = 1

<<<<<<< HEAD
=======

>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
class PizzaState:
    none = 0
    rolled = 1
    sauced = 2
    baked = 3

<<<<<<< HEAD
=======

>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
class ToppingType(int, Enum):
    none = 0
    dough = 1
    cheese = 2
    pepperoni = 3
    sausage = 4
    canadian_ham = 5
    mushrooms = 6
    peppers = 7
    chicken = 8
    olives = 9
    anchovies = 10
