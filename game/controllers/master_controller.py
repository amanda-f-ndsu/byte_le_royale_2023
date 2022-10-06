from copy import deepcopy
from tkinter import EventType

from game.common.action import Action
from game.common.enums import *
from game.common.player import Player
from game.common.stats import GameStats
import game.config as config
from game.utils.thread import CommunicationThread
from game.controllers.movement_controller import MovementController
from game.controllers.controller import Controller
from game.controllers.dispenser_controller import DispenserController
from game.controllers.oven_controller import OvenController

class MasterController(Controller):
    def __init__(self):
        super().__init__()
        self.game_over = False
        self.event_active = None
        self.event_timer = GameStats.event_timer
        self.event_times = None
        self.turn = None
        self.current_world_data = None
        self.movement_controller = MovementController()
        self.dispenser_controller = DispenserController()
        self.oven_controller = OvenController()


    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, clients):
        for index, client in enumerate (clients):
            pass

    # Generator function. Given a key:value pair where the key is the identifier for the current world and the value is
    # the state of the world, returns the key that will give the appropriate world information
    def game_loop_logic(self, start=1):
        self.turn = start

        # Basic loop from 1 to max turns
        while True:
            #logic for electrical event
            isPowerOut = False
            if self.event_active == EventType.eletrical:
                listOfOvens =  self.current_world_data["game_map"].ovens() 
                for oven in listOfOvens:
                    oven.power_outage()
                    isPowerOut = True
            else:
                if not isPowerOut:
                    listOfOvens =  self.current_world_data["game_map"].ovens() 
                for oven in listOfOvens:
                    oven.power_reset()
                    isPowerOut = False

            # Wait until the next call to give the number
            yield str(self.turn)
            # Increment the turn counter by 1
            self.turn += 1


    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, clients, world, turn):
        self.current_world_data = world

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client, turn):
        actions = Action()
        client.action = actions

        # Create deep copies of all objects sent to the player
        # Obfuscate data in objects that that player should not be able to see

        args = (self.turn, actions, self.current_world_data)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, clients, turn):
        # event logic 
        if(self.turn == self.event_times[0] or self.event_times[1]):
            pass
        self.oven_controller.handle_actions(self.current_world_data["game_map"].ovens())
        
        for client in clients:
            self.movement_controller(self.current_world_data["game_map"], client)
        self.dispenser_controller.handle_actions()
        
        if(self.event_timer == 0):
            self.event_active = None
            self.event_timer = GameStats.event_timer
        else:
            self.event_timer = self.event_timer -1
        

    # Return serialized version of game
    def create_turn_log(self, clients, turn):
        data = dict()

        # Add things that should be thrown into the turn logs here
        data['temp'] = None

        return data

    # Gather necessary data together in results file
    def return_final_results(self, clients, turn):
        data = dict()

        data['players'] = list()
        # Determine results
        for client in clients:
            data['players'].append(client.to_json())

        return data
