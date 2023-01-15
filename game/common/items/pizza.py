from game.common.enums import *
from game.common.items.item import Item
from game.common.items.topping import Topping
import json


class Pizza(Item):

    def __init__(self, worth: int = 0, quality: float = 1, state: int = PizzaState.rolled):
        super().__init__(worth, quality)
        self.object_type = ObjectType.pizza
        self.state = state
        self.__toppings = [] 
    
    @property
    def state(self):
        return self.__state
   
    @state.setter
    def state(self, state: int):
        if isinstance(state, int) and state in PizzaState.__dict__.values():
            self.__state = state

    @property
    def toppings(self):
        return self.__toppings
    
    def add_topping(self, topping: Topping):
        if self.state != PizzaState.sauced \
                or not isinstance(topping, Topping) \
                or topping.topping_type == ToppingType.dough:
            return topping
        if len(self.toppings) == 0 and topping.topping_type == ToppingType.cheese:
            self.__toppings.append(topping)
            return None
        elif len(self.toppings) in range(1, 4):
            self.__toppings.append(topping)
            return None
        else:
            return topping

    def to_json(self):
        data = super().to_json()
        data['state'] = self.state
        data['toppings'] = [topping.to_json() for topping in self.__toppings]
        return data

    def from_json(self, data: dict) -> 'Pizza':
        super().from_json(data)
        self.state = data['state']
        self.__toppings = []
        for item in data['toppings']:
            self.__toppings.append(Item(data["worth"], data["quality"]))
        return self
