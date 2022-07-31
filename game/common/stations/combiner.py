from game.common.cook import Cook
from game.common.stations.station import Station
from game.common.enums import ObjectType, PizzaState, ToppingType


class Combiner(Station):
    
    def __init__(self):
        super().__init__(None)
        self.object_type: ObjectType = ObjectType.combiner

    def take_action(self, cook: Cook):
        #Check if a pizza is stored in station
        if not self.item:
            #Check if the item passed is a sauced pizza
            if cook.held_item.object_type == ObjectType.pizza and cook.held_item.state == PizzaState.sauced:
                self.item = cook.held_item
                return None
            return None

        #If no item is being passed, return the stored pizza and set stored pizza to None
        if not cook.held_item:
            pizza = self.item
            self.item = None
            return pizza

        #Check if item is topping
        if cook.held_item.object_type == ObjectType.topping and cook.held_item.is_cut:
            if len(self.item.toppings) == 0:
                if cook.held_item.topping_type == ToppingType.cheese:
                    self.item.add_topping(cook.held_item)
            else:
                self.item.add_topping(cook.held_item)
            return None

    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Combiner':
        super().from_json(data)
        return self