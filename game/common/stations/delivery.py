from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.enums import ObjectType
from game.common.stations.station import Station
from game.common.stats import GameStats


class Delivery(Station):
    def __init__(self, item: Item = None, is_infested: bool = False):
        super().__init__(item, is_infested)
        self.object_type = ObjectType.delivery

    def take_action(self, cook: Cook = None):
        # Is it a pizza
        if not isinstance(cook.held_item, Pizza):
            return cook.held_item
        
        # Is the pizza baked (if it is baked, then it also has cheese)
        if cook.held_item.state != PizzaState.baked:
            return cook.held_item

        # Basic pizza, normal score calculation
        # Score = (base + sum of toppings) x (quality of pizza)
        score = GameStats.topping_stats[ToppingType.dough]["score"]
        for top in cook.held_item.toppings:
            score += int(top.worth * top.quality)
        score *= cook.held_item.quality
        score = int(score)
        # Add score to the cook
        cook.score += score
        # Return none to take the pizza from the cook
        return None

    def to_json(self) -> dict:
        data = super().to_json()
        return data

    def from_json(self, data: dict) -> 'Delivery':
        super().from_json(data)
        return self
