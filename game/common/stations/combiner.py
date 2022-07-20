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

    def take_action(self, item):
        #Check if a pizza is stored in station
        if(self.stored_pizza==None):
            #Check if the item passed is a sauced pizza
            if(item.object_type == ObjectType.pizza and item.state == PizzaState.sauced):
                self.stored_pizza = item
                return None
            return None

        #If no item is being passed, return the stored pizza and set stored pizza to None
        if(item==None):
            pizza = self.stored_pizza
            self.stored_pizza = None
            return pizza

        #Check if item is topping
        if(item.object_type == ObjectType.topping and item.is_cut == True):
            if(len(self.stored_pizza.toppings) == 0):
                if(item.topping_type == ToppingType.cheese):
                    self.stored_pizza.add_topping(item.topping_type)
            else:
                self.stored_pizza.add_topping(item.topping_type)
            return None


    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['stored_pizza'] = self.stored_pizza
        return dict_data

    def from_json(self, data: dict) -> 'Combiner':
        super().from_json(data)
        self.stored_pizza = data['stored_pizza']
        return self