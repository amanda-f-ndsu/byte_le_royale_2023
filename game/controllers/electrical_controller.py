
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *

class ElectricalEvent(Controller):

    def __init__(self):
       super().__init__()
    
    def handle_actions(self):
        print("hello")
    