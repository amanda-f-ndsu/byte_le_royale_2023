from game.common.stations.combiner import Combiner
from game.common.stations.storage import Storage
from game.common.stats import GameStats
from game.controllers.controller import Controller

class DecayController(Controller):
    def __init__(self):
        super().__init__()
    
    def handle_actions(self, stationList, playerList):
        #Check for items in combiners and storage
        #Also check for items held by the player
        #Then decay them by the decay rate
        #THe infestation speeds up decay on everything BUT what the cook is holding
        for station in stationList:
            if isinstance(station, Storage) or isinstance(station, Combiner) and station.item:
                if station.is_infested:
                    station.item.quality = max(station.item.quality - GameStats.infested_decay_rate, 0)
                else:
                    station.item.quality = max(station.item.quality - GameStats.decay_rate, 0)
        for cook in playerList:
            if cook.held_item:
                cook.held_item.quality = max(cook.held_item.quality - GameStats.decay_rate, 0)


