from copy import deepcopy
import random

from game.common.action import Action
from game.common.cook import Cook
from game.common.enums import *
from game.common.player import Player
from game.common.stats import GameStats
import game.config as config
from game.controllers.decay_controller import DecayController
from game.controllers.wet_tiles_controller import WetTilesController
from game.utils.thread import CommunicationThread
from game.controllers.movement_controller import MovementController
from game.controllers.controller import Controller
from game.controllers.dispenser_controller import DispenserController
from game.controllers.oven_controller import OvenController
from game.controllers.interact_controller import InteractController

class MasterController(Controller):
    def __init__(self):
        super().__init__()
        self.game_over = False
        self.event_active = None
        self.event_timer = GameStats.event_timer
        self.event_times = (5,100)
        self.turn = None
        self.current_world_data = None
        self.movement_controller = MovementController()
        self.dispenser_controller = DispenserController()
        self.oven_controller = OvenController()
        self.interact_controller = InteractController()
        self.decay_controller = DecayController()
        self.wet_tiles_controller = WetTilesController()


    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, clients):
        starting_positions = [[3,3],[3, 9]]
        for index, client in enumerate (clients):
            client.cook = Cook(position=starting_positions[index])

    # Generator function. Given a key:value pair where the key is the identifier for the current world and the value is
    # the state of the world, returns the key that will give the appropriate world information
    def game_loop_logic(self, start=1):
        self.turn = start

        # Basic loop from 1 to max turns
        while True:
            # Wait until the next call to give the number
            yield str(self.turn)
            # Increment the turn counter by 1
            self.turn += 1


    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, clients, world, turn):
        self.current_world_data = world
        random.seed(world["seed"])

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client, turn):
        turn_action = Action()
        client.action = turn_action

        # Create deep copies of all objects sent to the player
        current_world = deepcopy(self.current_world_data["game_map"])
        copy_cook = deepcopy(client.cook)
        # Obfuscate data in objects that that player should not be able to see
        # Currently world data isn't obfuscated at all
        args = (self.turn, turn_action, current_world, copy_cook)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, clients, turn):
        for client in clients:
            self.movement_controller.handle_actions(self.current_world_data["game_map"], client)
            self.interact_controller.handle_actions(client,self.current_world_data["game_map"])
        self.dispenser_controller.handle_actions(self.current_world_data["game_map"],turn)
        for oven in self.current_world_data["game_map"].ovens():
            self.oven_controller.handle_actions(oven)
        # checks event logic at the end of round
        self.handle_events(clients)
        
       
    def handle_events(self, clients):
        # If it is time to run an event, master controller picks an event to run
        if(self.turn == self.event_times[0] or self.turn == self.event_times[1]):
            self.event_active = random.randint(EventType.electrical,EventType.wet_tile)
        # Check if electrical event is triggered 
        listOfOvens = self.current_world_data["game_map"].ovens() 
        if self.event_active == EventType.electrical and self.event_timer == GameStats.event_timer:
                for oven in listOfOvens:
                    oven.is_powered = False
        # Check if wet tiles event is triggered
        if self.event_active == EventType.wet_tile and self.event_timer == GameStats.event_timer:
            if not self.wet_tiles_controller.handle_actions(self.current_world_data["game_map"],self.current_world_data["game_map"].cooks()):
               self.event_active = random.randint(EventType.electrical,EventType.infestation) 
        # Event stops running once timer hits zero, timer is reset
        if self.event_timer == 0:
            if self.event_active == EventType.electrical:
                    for oven in listOfOvens:
                        oven.is_powered = True
            if self.event_active == EventType.wet_tile:
                for y in range(7):
                    for x in range(13):
                        self.current_world_data["game_map"].game_map[y][x].is_wet_tile = False 
            self.event_active = EventType.none
            self.event_timer = GameStats.event_timer
        # timer counts down when event is running
        if self.event_active != EventType.none:
            self.event_timer = self.event_timer -1
        #Decay always occurs end of turn
        self.decay_controller.handle_actions(self.event_active,self.current_world_data["game_map"].game_map,self.current_world_data["game_map"].cooks())
            
        


    # Return serialized version of game
    def create_turn_log(self, clients, turn):
        data = dict()
        data['tick'] = turn
        data['event_active'] = self.event_active
        data['clients'] = [client.to_json() for client in clients]
        # Add things that should be thrown into the turn logs here
        data['game_map'] = self.current_world_data["game_map"].to_json()

        return data

    # Gather necessary data together in results file
    def return_final_results(self, clients, turn):
        data = dict()

        data['players'] = list()
        # Determine results
        for client in clients:
            data['players'].append(client.to_json())

        return data
