from game.common.dispenser import Dispenser
from game.controllers.controller import Controller
from game.common.enums import *

class DispenserController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, world):
        for tile in world:
            if isinstance(tile.occupied_by,Dispenser):
                tile.occupied_by.dispense()
                         