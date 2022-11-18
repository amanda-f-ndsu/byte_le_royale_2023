import unittest

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
        self.player = Player()
        board = generate_map(5)
        self.world = board
        cooks = board.cooks()
        self.player.cook = cooks[0]
        self.movementController = MovementController()
        

    #def test_interact_Bin(self):
    #    self.player.cook.chosen_action = ActionType.Move.up
    #    self.movementController.handle_actions(self.world,self.player)
    #    self.player.cook.chosen_action = ActionType.Move.up
    #    self.movementController.handle_actions(self.world,self.player)
    #    self.player.cook.held_item = Pizza(PizzaState.sauced)
    #    self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
    #    self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
    #    self.assertEqual(self.player.cook.held_item, None)

    def test_interact_upstorage(self):
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Topping(topping_type=ToppingType.pepperoni)
        temp: Topping = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertEqual(temp, None)

    def test_interact_storage(self):
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.up
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.right
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Topping(topping_type=ToppingType.pepperoni)
        temp: Topping = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertEqual(temp, None)
        

    #def test_interact_oven(self):
    #    self.player.cook.chosen_action = ActionType.Move.left
    #    self.movementController.handle_actions(self.world,self.player)
    #    self.player.cook.chosen_action = ActionType.Move.left
    #    self.movementController.handle_actions(self.world,self.player)
    #    self.player.cook.held_item = Pizza(PizzaState.sauced)
    #    self.player.cook.held_item.add_topping(Topping(topping_type=ToppingType.cheese))
    #    self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
    #    self.assertIsNotNone(self.player.cook.held_item.state, Pizza(PizzaState.sauced))
    
    #def test_interact_combiner(self):
    #    self.player.cook.chosen_action = ActionType.Move.right
    #    self.movementController.handle_actions(self.world,self.player)
    #    self.player.cook.chosen_action = ActionType.Move.right
    #    self.movementController.handle_actions(self.world,self.player)
    #    self.player.cook.held_item = Pizza(PizzaState.sauced)
    #    self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
    #    self.assertIsInstance(self.player.cook.held_item, Pizza)

    #def test_interact_down_delivery(self):
        #self.player.cook.chosen_action = ActionType.Move.down
        #self.movementController.handle_actions(self.world,self.player)
        #self.player.cook.chosen_action = ActionType.Move.down
        #self.movementController.handle_actions(self.world,self.player)
        #self.player.cook.held_item = Pizza(PizzaState.baked)
        #self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        #self.assertIsNone(self.player.cook.held_item)
        #self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        #self.assertIsInstance(self.player.cook.held_item, Pizza(PizzaState.sauced))

    def test_interact_dispenser(self):
        self.player.cook.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.down
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.chosen_action = ActionType.Move.left
        self.movementController.handle_actions(self.world,self.player)
        self.player.cook.held_item = Pizza()
        self.player.cook.held_item = self.interactController.handle_actions(self.player.cook, self.world)
        self.assertIsNotNone(self.player.cook.held_item)