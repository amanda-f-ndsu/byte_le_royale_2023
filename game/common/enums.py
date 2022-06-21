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
    dispenser = 4
    station = 5
    cook = 6
    
class ActionType:
    none = 0
    test = 1

class ToppingType:
    none = (0, 0)
    cheese = (1, 20)
    pepperoni = (2, 40)
    canadianham = (3, 40)
    mushrooms = (4, 40)
    peppers = (5, 50)
    chicken = (6, 40)
    olives = (7, 50)
    anchovies = (8, 50)
