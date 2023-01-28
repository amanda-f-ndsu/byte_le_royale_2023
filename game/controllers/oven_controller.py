
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.common.enums import *

class OvenController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, oven):
        if oven.is_active and oven.is_powered:
            if not oven.item:
                oven.timer = GameStats.oven_timer['start']
                oven.is_active = False
                return
            if oven.item.state == PizzaState.baked and oven.timer == 0:
                oven.item = None
            if oven.timer == GameStats.oven_timer['baked']:
                oven.item.state = PizzaState.baked
        
            oven.timer = oven.timer - 1
        
        if not oven.is_powered:
            oven.item = None
            oven.is_active = False
            oven.timer = GameStats.oven_timer['start']


                         