from game.common.stations.combiner import Combiner
from game.common.stations.storage import Storage
from game.common.stations.oven import Oven
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import EventType
from game.common.game_board import GameBoard

class DecayController(Controller):
    def __init__(self):
        super().__init__()
    
    def handle_actions(self, eventType, gameMap, playerList):
        #Check for items in combiners and storage
        #Also check for items held by the player
        #Then decay them by the decay rate
        #THe infestation speeds up decay on everything BUT what the cook is holding
        #The way to check infestation is by the eventType passed to handle_actions
        for row in gameMap:
            for station in row:
                if (isinstance(station, Storage) or isinstance(station, Combiner) or isinstance(station, Oven)) and station.item: #Currently, only storage, combiners and ovens actually hold items
                    if isinstance(station, Oven) and station.is_active:
                        continue #Skip ovens that are currently cooking
                    if eventType == EventType.infestation:
                        station.item.quality = max(station.item.quality - GameStats.infested_decay_rate, 0)
                        if station.item.quality <= 0:
                            station.item = None
                    else:
                        station.item.quality = max(station.item.quality - GameStats.decay_rate, 0)
                        if station.item.quality <= 0:
                            station.item = None
        for cook in playerList:
            if cook.held_item:
                cook.held_item.quality = max(cook.held_item.quality - GameStats.decay_rate, 0)
                if cook.held_item.quality <= 0:
                            cook.held_item = None


