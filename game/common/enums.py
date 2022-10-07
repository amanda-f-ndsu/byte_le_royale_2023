from enum import Enum

class DebugLevel:
    none = 0
    client = 1
    controller = 2
    engine = 3

class ObjectType:
    none = 0
    game_board = 1
    counter = 2
    action = 3
    player = 4
    item = 5
    dispenser = 6
    station = 7
    cook = 8
    topping = 9
    tile = 10
    pizza = 11
    roller = 12
    cutter = 13
    oven = 14
    bin = 15
    combiner = 16
    storage = 17
    delivery = 18
    sauce = 19


class ActionType:
    none = 0
    test = 1
    move = 2

class Move:
    none = 0.5
    up = 1.5
    down = 2.5
    left = 3.5
    right = 4.5

class PizzaState:
    none = 0
    rolled = 1
    sauced = 2
    baked = 3

class eventType:
    none = 0
    eletrical = 1
    infestation = 2
    wet_tile = 3


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
