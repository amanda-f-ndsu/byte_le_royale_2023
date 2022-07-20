from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.enums import ObjectType
from game.common.items.topping import Topping
from game.common.stations.station import Station
from game.common.stats import GameStats
import math

class Delivery(Station):
    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type = ObjectType.delivery

    def take_action(self, cook):
        #Is it a pizza
        if(cook.held_item.object_type != ObjectType.pizza):
            return cook.held_item
        
        #Is the pizza baked (if it is baked, then it also has cheese)
        if(cook.held_item.state != PizzaState.baked):
            return cook.held_item

        #Basic pizza, normal score calculation
        #Score = (base + sum of toppings) x (quality of pizza)
        score = GameStats.topping_stats[ToppingType.dough]["score"]
        for top in cook.held_item.toppings:
            score += (int)(math.floor((top.worth * top.quality)))
        score *= cook.held_item.quality
        score = math.floor(score)
        #Add score to the cook
        cook.score += score
        #Return none to take the pizza from the cook
        return None
        

    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Delivery':
        super().from_json(data)