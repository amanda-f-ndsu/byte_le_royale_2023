from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.enums import ObjectType
from game.common.items.topping import Topping
from game.common.stations.station import Station
from game.common.stats import GameStats

class Delivery(Station):
    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type = ObjectType.station #Does this need to be delivery?

    def take_action(self, item):
        #Is it a pizza
        if(item.object_type != ObjectType.pizza):
            return item
        
        #Is the pizza baked (if it is baked, then it also has cheese)
        if(item.state != PizzaState.baked):
            return item

        #Check if speical pizza
        #NEED TO IMPLEMENT

        #Basic pizza, normal score calculation
        #Score = (base + sum of toppings) x (time left + quality)
        score = GameStats.topping_stats[ToppingType.dough]["score"]
        for top in item.toppings:
            score += top.worth
        score *= item.quality
        return None
        

    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Delivery':
        super().from_json(data)