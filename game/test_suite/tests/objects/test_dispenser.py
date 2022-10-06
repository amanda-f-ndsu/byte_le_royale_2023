import unittest
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.dispenser import Dispenser


class TestDispenser(unittest.TestCase):
    def setUp(self):
      self.dispenser = Dispenser()
      self.cook = Cook()  
      
    def testDispenseEmpty(self):
        self.assertIsNone(self.dispenser.item)
        self.dispenser.dispense()
        self.assertIsNotNone(self.dispenser.item)

    def testDispenseFull(self):
        self.dispenser.item = Topping(topping_type=ToppingType.mushrooms)
        stored_item = self.dispenser.item # actual item stored in dispenser
        same_item = Topping(topping_type=ToppingType.mushrooms) # same item but different reference
        self.assertTrue(stored_item is self.dispenser.item)
        # test to prove that item isn't replaced after dispense method    
        self.dispenser.dispense()
        self.assertTrue(stored_item is self.dispenser.item)
        self.assertFalse(same_item is self.dispenser.item) # this case proves that the dispenser item isn't replaced by same topping object

    def testCookHandsEmpty(self):
        self.dispenser.item = Topping(topping_type=ToppingType.chicken)
        stored_item = self.dispenser.item # actual item stored in dispenser
        self.cook.held_item = self.dispenser.take_action(self.cook.held_item)
        self.assertTrue(stored_item is self.cook.held_item)
        self.assertIsNone(self.dispenser.item)


    def testCookHandsFull(self):
        self.dispenser.item = Topping(topping_type=ToppingType.olives)
        self.cook.held_item = Topping(topping_type=ToppingType.cheese)
        stored_item = self.dispenser.item # actual item stored in dispenser
        cook_item = self.cook.held_item
        self.cook.held_item = self.dispenser.take_action(self.cook.held_item)
        self.assertTrue(cook_item is self.cook.held_item)
        self.assertTrue(stored_item is self.dispenser.item)
    

    

if __name__ == '__main__':
    unittest.main()