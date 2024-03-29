import unittest
from game.controllers.decay_controller import DecayController
from game.common.enums import EventType
from game.common.enums import PizzaState
from game.common.stations.combiner import Combiner
from game.common.stations.storage import Storage
from game.common.stations.oven import Oven
from game.common.cook import Cook
from game.common.items.pizza import Pizza
from game.common.stats import GameStats
from game.common.map.tile import Tile

class TestDecayController(unittest.TestCase):

    def setUp(self):
        self.decayController = DecayController()
        self.stationList = [[]]
        self.playerList = []
        self.eventType = EventType.none
        # Create stations
        self.combiner =  Combiner()
        self.combiner.item =  Pizza(0, 1, PizzaState.rolled)
        self.storage =  Storage()
        self.storage.item =  Pizza(0, 1, PizzaState.rolled)
        # Create player
        self.player =  Cook()
        self.player.held_item =  Pizza(0, 1, PizzaState.rolled)
        # Add to lists
        self.stationList[0].append(Tile(self.combiner))
        self.stationList[0].append(Tile(self.storage))
        self.playerList.append(self.player)

    
    def testStationsAndCooks(self):
        # Test an combiner, storage, and cook
        targetNum = 1 - GameStats.decay_rate
        self.decayController.handle_actions(self.eventType, self.stationList, self.playerList)
        # Stations
        self.assertEqual(self.combiner.item.quality, targetNum)
        self.assertEqual(self.storage.item.quality, targetNum)
        # Player
        self.assertEqual(self.player.held_item.quality, targetNum)
    
    def testStationsAndCooksInfested(self):
        # Test an combiner, storage, and cook while infested
        decayNum = 1 - GameStats.decay_rate
        infestedDecayNum = 1 - GameStats.infested_decay_rate
        self.eventType = EventType.infestation
        self.decayController.handle_actions(self.eventType, self.stationList, self.playerList)
        # Stations
        self.assertEqual(self.combiner.item.quality, infestedDecayNum)
        self.assertEqual(self.storage.item.quality, infestedDecayNum)
        # Player
        self.assertEqual(self.player.held_item.quality, decayNum)
    
   