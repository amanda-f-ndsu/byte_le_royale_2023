from enum import Enum
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



