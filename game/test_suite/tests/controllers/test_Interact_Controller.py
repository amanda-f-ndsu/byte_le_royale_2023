import unittest
<<<<<<< HEAD
=======
from game.common.action import Action
>>>>>>> 178d08184c392d29cef9e67c56c5ba54d608436b

from game.common.cook import Cook
from game.common.enums import *
from game.common.map.counter import Counter
from game.common.player import Player
from game.controllers.interact_controller import InteractController
from game.utils.generate_game import generate_map
from game.controllers.movement_controller import MovementController
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping
from game.common.stations.oven import Oven
from game.controllers.oven_controller import OvenController
from game.common.stats import GameStats

class TestInteractController(unittest.TestCase):
    def setUp(self):
        self.interactController = InteractController()
<<<<<<< HEAD
        self.player = Player()
=======
        self.player = Player(action = Action())
>>>>>>> 178d08184c392d29cef9e67c56c5ba54d608436b
        board = generate_map(5)
        self.world = board
        cooks = board.cooks()
        self.player.cook = cooks[0]
        self.movementController = MovementController()
        

<<<<<<< HEAD
    def test_interact_Oven(self):
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza()
        self.player.cook.held_item.state = PizzaState.sauced 
        self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNone(self.player.cook.held_item)

    def test_interact_roller(self):
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Topping()
        self.player.cook.held_item.topping_type = ToppingType.dough
        temp = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsInstance(temp, Pizza)

    def test_interact_Cutter(self):
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Topping()
        self.player.cook.held_item.topping_type = ToppingType.pepperoni
        temp = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertEqual(temp.is_cut, True)
        

    def test_interact_bin(self):
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza(PizzaState.sauced)
        self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNone(self.player.cook.held_item)

    def test_interact_storage(self):
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza(PizzaState.sauced)
        self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNone(self.player.cook.held_item)
    
    def test_interact_delivery(self):
        self.player.cook.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza()
        self.player.cook.held_item.state = PizzaState.baked
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNone(self.player.cook.held_item)

    def test_interact_combiner(self):
        self.player.cook.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza()
        self.player.cook.held_item.state = PizzaState.sauced
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNone(self.player.cook.held_item)
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsInstance(self.player.cook.held_item, Pizza)

    def test_interact_sauce(self):
        self.player.cook.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza()
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertEqual(self.player.cook.held_item.state, PizzaState.sauced)
=======
    def test_interact_Bin(self):
        self.player.action.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza(PizzaState.sauced)
        self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
        self.player.action.chosen_action = ActionType.interact
        self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
        self.assertEqual(self.player.cook.held_item, None)

    def test_interact_upstorage(self):
        self.player.action.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Topping(topping_type=ToppingType.pepperoni)
        self.player.action.chosen_action = ActionType.interact
        temp: Topping = self.interactController.handle_actions(self.player, self.world)
        self.assertEqual(temp, None)

    def test_interact_storage(self):
        self.player.action.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Topping(topping_type=ToppingType.pepperoni)
        self.player.action.chosen_action = ActionType.interact
        temp: Topping = self.interactController.handle_actions(self.player, self.world)
        self.assertEqual(temp, None)
        

    def test_interact_oven(self):
       self.player.action.chosen_action = ActionType.Move.up
       self.movementController.handle_actions(self.world,self.player)
       self.player.action.chosen_action = ActionType.Move.up
       self.movementController.handle_actions(self.world,self.player)
       self.player.cook.held_item = Pizza(PizzaState.sauced)
       self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
       self.player.action.chosen_action = ActionType.interact
       self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
       self.assertIsNotNone(self.player.cook.held_item.state, Pizza(PizzaState.sauced))
    
    def test_interact_combiner(self):
       self.player.action.chosen_action = ActionType.Move.down
       self.movementController.handle_actions(self.world,self.player)
       self.player.action.chosen_action = ActionType.Move.down
       self.movementController.handle_actions(self.world,self.player)
       self.player.cook.held_item = Pizza(state=PizzaState.sauced)
       self.player.action.chosen_action = ActionType.interact
       self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
       self.assertIsNone(self.player.cook.held_item, Pizza)
       self.player.cook.held_item = Topping(topping_type=ToppingType.cheese, is_cut=True)
       self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
       self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
       self.assertIsInstance(self.player.cook.held_item, Pizza)

    def test_interact_down_delivery(self):
        self.player.action.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza(state=PizzaState.baked)
        self.player.action.chosen_action = ActionType.interact
        self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
        self.assertIsNone(self.player.cook.held_item)

    def test_interact_dispenser(self):
        self.player.action.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.action.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza()
<<<<<<< HEAD
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNotNone(self.player.cook.held_item)
>>>>>>> 178d08184c392d29cef9e67c56c5ba54d608436b
=======
        self.player.action.chosen_action = ActionType.interact
        self.player.cook.held_item = self.interactController.handle_actions(self.player, self.world)
        self.assertIsNotNone(self.player.cook.held_item)
>>>>>>> 90e5653fc204fed8b6bc87eb355f5d31cbfa1773
