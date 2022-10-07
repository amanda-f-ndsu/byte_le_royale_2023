import unittest
from game.common.enum import EventType
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
        self.combiner = new Combiner()
        self.combiner.item = new Pizza(0, 100, PizzaState.rolled)
        self.storage = new Storage()
        self.storage.item = new Pizz(0, 100, PizzaState.rolled)
        self.ovenOff = new Oven()
        self.ovenOff.item = new Pizza(0, 100, PizzaState.sauced)
        self.ovenOn = new Oven()
        self.ovenOn.is_active = true
        self.ovenOn.item = new Pizza(0, 100, PizzaState.sauced)
        # Create player
        self.player = new Cook()
        self.player.held_item = new Pizz(0, 100, PizzaState.rolled)
        # Add to lists
        self.stationList.append(combiner)
        self.stationList.append(storage)
        self.stationList.append(ovenOff)
        self.stationList.append(ovenOn)
        self.playerList.append(player)

    
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
    
   