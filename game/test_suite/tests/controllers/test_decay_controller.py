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

class TestDecayController(unittest.TestCase):

    def setUp(self):
        self.decayController = DecayController()
        self.stationList = []
        self.playerList = []
        self.eventType = EventType.none
        # Create stations
        self.combiner =  Combiner()
        self.combiner.item =  Pizza(0, 100, PizzaState.rolled)
        self.storage =  Storage()
        self.storage.item =  Pizza(0, 100, PizzaState.rolled)
        self.ovenOff =  Oven()
        self.ovenOff.item =  Pizza(0, 100, PizzaState.sauced)
        self.ovenOn =  Oven()
        self.ovenOn.is_active = True
        self.ovenOn.item =  Pizza(0, 100, PizzaState.sauced)
        # Create player
        self.player =  Cook()
        self.player.held_item =  Pizza(0, 100, PizzaState.rolled)
        # Add to lists
        self.stationList.append(self.combiner)
        self.stationList.append(self.storage)
        self.stationList.append(self.ovenOff)
        self.stationList.append(self.ovenOn)
        self.playerList.append(self.player)

    
    def testStationsAndCooks(self):
        # Test an oven, combiner, storage, and cook
        targetNum = 100 - GameStats.decay_rate
        self.decayController.handle_actions(self.eventType, self.stationList, self.playerList)
        # Stations
        self.assertEqual(self.combiner.item.quality, targetNum)
        self.assertEqual(self.storage.item.quality, targetNum)
        self.assertEqual(self.ovenOff.item.quality, targetNum)
        self.assertEqual(self.ovenOn.item.quality, 100)
        # Player
        self.assertEqual(self.player.helf_item.quality, targetNum)
    
    def testStationsAndCooksInfested(self):
        # Test an oven, combiner, storage, and cook while infested
        decayNum = 100 - GameStats.decay_rate
        infestedDecayNum = 100 - GameStats.infested_decay_rate
        self.eventType = EventType.infestation
        self.decayController.handle_actions(self.eventType, self.stationList, self.playerList)
        # Stations
        self.assertEqual(self.combiner.item.quality, infestedDecayNum)
        self.assertEqual(self.storage.item.quality, infestedDecayNum)
        self.assertEqual(self.ovenOff.item.quality, infestedDecayNum)
        self.assertEqual(self.ovenOn.item.quality, 100)
        # Player
        self.assertEqual(self.player.helf_item.quality, decayNum)
    
   