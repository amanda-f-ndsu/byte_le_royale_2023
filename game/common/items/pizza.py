from game.common.enums import ObjectType, PizzaState
from game.common.items.item import Item
import json


class Pizza(Item):

    def __init__(self, worth: int, quality: float = 0, state: int = PizzaState.rolled):
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


    """Not allowed for client use! Will be disqualified if called in contestant's code"""
    def add_topping(self, topping: int):
        if len(self.toppings) < 4 and isinstance(topping, int) : # and topping in Toppings.__dict__.values() <-- will add when toppings merged in
            self.toppings.append(topping)
    

    def to_json(self):
      data = super().to_json()
      data['state'] = self.state
      data['toppings'] = json.dumps(self.__toppings)
      return data
        

    def from_json(self, data: dict) -> 'Pizza':
      super().from_json(data)
      self.state = data['state']
      self.__toppings = json.loads(data['toppings'])
      return self
      

