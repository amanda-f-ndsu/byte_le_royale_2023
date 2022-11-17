import unittest
from game.common.cook import Cook
from game.common.stations.dispenser import Dispenser
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stats import GameStats



class TestDispenser(unittest.TestCase):
    def setUp(self):
      self.dispenser = Dispenser()
      self.cook = Cook()  
      
    def testDispenseEmpty(self):
        self.assertIsNone(self.dispenser.item)
        self.dispenser.dispense()
        self.assertIsNotNone(self.dispenser.item)

    def testDispenseFull(self):
        self.dispenser.item = Topping(topping_type=ToppingType.mushrooms, quality=1, worth=GameStats.topping_stats[ToppingType.mushrooms]["score"])
        stored_item = self.dispenser.item # actual item stored in dispenser
        same_item = Topping(topping_type=ToppingType.mushrooms, quality=1, worth=GameStats.topping_stats[ToppingType.mushrooms]["score"]) # same item but different reference
        self.assertTrue(stored_item is self.dispenser.item)
        # test to prove that item isn't replaced after dispense method    
        self.dispenser.dispense()
        self.assertTrue(stored_item is self.dispenser.item)
        self.assertFalse(same_item is self.dispenser.item) # this case proves that the dispenser item isn't replaced by same topping object

    def testCookHandsEmpty(self):
        self.dispenser.item = Topping(topping_type=ToppingType.chicken, quality=1, worth=GameStats.topping_stats[ToppingType.chicken]["score"])
        stored_item = self.dispenser.item # actual item stored in dispenser
        self.cook.held_item = self.dispenser.take_action(self.cook)
        self.assertTrue(stored_item is self.cook.held_item)
        self.assertIsNone(self.dispenser.item)


    def testCookHandsFull(self):
        self.dispenser.item = Topping(topping_type=ToppingType.olives, quality=1, worth=GameStats.topping_stats[ToppingType.olives]["score"])
        self.cook.held_item = Topping(topping_type=ToppingType.cheese, quality=1, worth=GameStats.topping_stats[ToppingType.cheese]["score"])
        stored_item = self.dispenser.item # actual item stored in dispenser
        cook_item = self.cook.held_item
        self.cook.held_item = self.dispenser.take_action(self.cook)
        self.assertTrue(cook_item is self.cook.held_item)
        self.assertTrue(stored_item is self.dispenser.item)
    

    

if __name__ == '__main__':
    unittest.main()