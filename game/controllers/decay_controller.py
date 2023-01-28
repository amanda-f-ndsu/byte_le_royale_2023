from game.common.stations.combiner import Combiner
from game.common.stations.storage import Storage
from game.common.stations.oven import Oven
from game.common.stations.station import Station
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import EventType
from game.common.game_board import GameBoard

class DecayController(Controller):
    def __init__(self):
        super().__init__()
        self.is_infested = False
    
    def handle_actions(self, eventType, gameMap, playerList):
        #Check for items in combiners and storage
        #Also check for items held by the player
        #Then decay them by the decay rate
        #THe infestation speeds up decay on everything BUT what the cook is holding
        #The way to check infestation is by the eventType passed to handle_actions

        # Check for updating the infestation tags on the stations
        if eventType == EventType.infestation and not self.is_infested:
            self.is_infested = True
            self.infest_board(gameMap)
        elif eventType != EventType.infestation and self.is_infested:
            self.is_infested = False
            self.clear_infest(gameMap)

        for row in gameMap:
            for station in row:
                if station.occupied_by == None:
                    continue
                station = station.occupied_by
                if (isinstance(station, Storage) or isinstance(station, Combiner)) and station.item: #Currently, only storage and combiners
                    if eventType == EventType.infestation:
                        station.item.quality = max(station.item.quality - GameStats.infested_decay_rate, 0)
                    else:
                        station.item.quality = max(station.item.quality - GameStats.decay_rate, 0)
                    if station.item.quality <= 0:
                            station.item = None
        for cook in playerList:
            if cook.held_item:
                cook.held_item.quality = max(cook.held_item.quality - GameStats.decay_rate, 0)
                if cook.held_item.quality <= 0:
                            cook.held_item = None


    def infest_board(self, gameMap: GameBoard):
        for row in gameMap:
            for station in row:
                if station.occupied_by == None:
                    continue
                station = station.occupied_by
                if not isinstance(station, Station):
                    continue
                if isinstance(station, Storage) or isinstance(station, Combiner):
                    station.is_infested = True

    def clear_infest(self, gameMap: GameBoard):
        for row in gameMap:
            for station in row:
                if station.occupied_by == None:
                    continue
                station = station.occupied_by
                if not isinstance(station, Station):
                    continue
                if isinstance(station, Storage) or isinstance(station, Combiner):
                    station.is_infested = False