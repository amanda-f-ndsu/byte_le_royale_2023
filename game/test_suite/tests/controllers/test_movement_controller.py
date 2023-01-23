import unittest
<<<<<<< HEAD
=======
from game.common.action import Action
>>>>>>> 178d08184c392d29cef9e67c56c5ba54d608436b

from game.common.cook import Cook
from game.common.enums import *
from game.common.map.counter import Counter
from game.common.player import Player
from game.controllers.movement_controller import MovementController
from game.utils.generate_game import generate_map


class TestMovementController(unittest.TestCase):
    
    def setUp(self):
        self.movementController = MovementController()
        board = generate_map(5)
        self.player = Player() # initial position is (3,3)
        cooks = board.cooks()
        self.player.cook = cooks[0]
        self.world = board

    def test_init_pos(self):
        self.assertTrue(self.player.cook.position == (3,3))
        self.assertTrue(isinstance(self.world.game_map[3][3].occupied_by, Cook))
    
    def test_up(self):
        self.player.action = Action(ActionType.Move.up)
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (2,3))
        self.assertIsNone(self.world.game_map[3][3].occupied_by)
        self.assertTrue(isinstance(self.world.game_map[2][3].occupied_by, Cook))


    def test_down(self):
        self.player.action = Action(ActionType.Move.down)
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (4,3))
        self.assertIsNone(self.world.game_map[3][3].occupied_by)
        self.assertTrue(isinstance(self.world.game_map[4][3].occupied_by, Cook))


    def test_left(self):
        self.player.action = Action(ActionType.Move.left)
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (3,2))
        self.assertIsNone(self.world.game_map[3][3].occupied_by)
        self.assertTrue(isinstance(self.world.game_map[3][2].occupied_by, Cook))

    def test_right(self):
        self.player.action = Action(ActionType.Move.right)
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (3,4))
        self.assertIsNone(self.world.game_map[3][3].occupied_by)
        self.assertTrue(isinstance(self.world.game_map[3][4].occupied_by, Cook))

    def test_move_fail_up(self):
        self.player.action = Action(ActionType.Move.up)
        self.world.game_map[2][3].occupied_by = Counter()
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (3,3))

    def test_move_fail_down(self):
        self.player.action = Action(ActionType.Move.down)
        self.world.game_map[4][3].occupied_by = Counter()
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (3,3))

    def test_move_fail_left(self):
        self.player.action = Action(ActionType.Move.left)
        self.world.game_map[3][2].occupied_by = Counter()
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (3,3))

    def test_move_fail_right(self):
        self.player.action = Action(ActionType.Move.right)
        self.world.game_map[3][4].occupied_by = Counter()
        self.movementController.handle_actions(self.world,self.player)
        self.assertTrue(self.player.cook.position == (3,3))

    def test_wet_tile(self):
        self.player.action = Action(ActionType.Move.right)
        self.world.game_map[3][4].is_wet_tile = True
        self.movementController.handle_actions(self.world,self.player)
        print(self.player.cook.position)
        self.assertTrue(self.player.cook.position == (3,3))