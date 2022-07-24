from game.common.cook import Cook
from game.common.stations.station import Station
from game.common.enums import ObjectType, PizzaState, ToppingType
from game.common.items.item import Item
from game.common.items.topping import Topping
from game.common.items.pizza import Pizza

class Combiner(Station):
    
    def __init__(self):
        super().__init__(None)
        self.object_type:ObjectType = ObjectType.combiner
        self.stored_pizza:Pizza = None

    @property
    def stored_pizza(self) -> Pizza:
        return self.__stored_pizza

    @stored_pizza.setter
    def stored_pizza(self, stored_pizza: Pizza):
        self.__stored_pizza = stored_pizza

    def take_action(self, cook: Cook):
        #Check if a pizza is stored in station
        if(self.stored_pizza==None):
            #Check if the item passed is a sauced pizza
            if(cook.held_item.object_type == ObjectType.pizza and cook.held_item.state == PizzaState.sauced):
                self.stored_pizza = cook.held_item
                return None
            return None

        #If no item is being passed, return the stored pizza and set stored pizza to None
        if(cook.held_item==None):
            pizza = self.stored_pizza
            self.stored_pizza = None
            return pizza

        #Check if item is topping
        if(cook.held_item.object_type == ObjectType.topping and cook.held_item.is_cut == True):
            if(len(self.stored_pizza.toppings) == 0):
                if(cook.held_item.topping_type == ToppingType.cheese):
                    self.stored_pizza.add_topping(cook.held_item)
            else:
                self.stored_pizza.add_topping(cook.held_item)
            return None


    def to_json(self) -> dict:
        dict_data = super().to_json()
<<<<<<< HEAD
        dict_data['stored_pizza'] = self.stored_pizza if self.stored_pizza is not None else None
=======
        dict_data['stored_pizza'] = self.stored_pizza
>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
        return dict_data

    def from_json(self, data: dict) -> 'Combiner':
        super().from_json(data)
<<<<<<< HEAD
        self.stored_pizza = data['stored_pizza'] if self.stored_pizza is not None else None
=======
        self.stored_pizza = data['stored_pizza']
>>>>>>> 9006bcee3c80c3538d3a07d1a854db357808081c
        return self