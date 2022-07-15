import unittest
from game.common.cutter import Cutter
from game.common.enums import *
from game.common.items.topping import Topping

class TestOven(unittest.TestCase):
    def setUp(self):
        self.topping = Topping(quality=4, worth=20, topping_type=ToppingType.canadian_ham, is_cut=False)
        self.cutter = Cutter(self.topping)


    def testTakeAction(self):
        self.topping = self.cutter.take_action(self.topping)
        self.assertEqual(self.topping.topping_type, ToppingType.canadian_ham)
        self.assertEqual(self.topping.is_cut, True)

    def testTakeAction_nocut(self):
        self.topping.topping_type = ToppingType.dough
        self.topping = self.cutter.take_action(self.topping)
        self.assertEqual(self.topping.topping_type, ToppingType.dough)
        self.assertEqual(self.topping.is_cut, False)

    def testTakeAction_none(self):
        self.topping = None
        self.topping = self.cutter.take_action(self.topping)
        self.assertIsNone(self.topping)





if __name__ == '__main__':
    unittest.main()