import random
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.item import Item
from game.common.items.topping import Topping
from game.common.stations.station import Station
from game.common.stats import GameStats



class Dispenser(Station):

    def __init__(self, item: Item = None, is_infested : bool = False):
        super().__init__(item,is_infested)
        self.object_type: ObjectType = ObjectType.dispenser

   
    def take_action(self, cook: Cook):
       rtn_item = cook.held_item
       if not rtn_item and self.item:
          rtn_item = self.item
          self.item = None
       return rtn_item
        
       

    def dispense(self, turn):
        if not self.item or turn % GameStats.turns_per_item_turnover_event == 0:
            rand_topping = random.randint(ToppingType.dough, ToppingType.anchovies)
            self.item = Topping(topping_type=rand_topping, worth=GameStats.topping_stats[rand_topping]["score"], quality=1)

    def to_json(self) -> dict:
        dict_data = super().to_json()
        return dict_data

    def from_json(self, data: dict) -> 'Dispenser':
        super().from_json(data)
        return self
   

    def obfuscate(self) -> None:
        super().obfuscate()
        pass

