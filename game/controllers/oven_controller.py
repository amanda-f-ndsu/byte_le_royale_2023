
from game.controllers.controller import Controller
from game.common.cook import Cook
from game.common.enums import *
from game.common.items.pizza import Pizza

class OvenController(Controller):

    def __init__(self):
       super().__init__()
     
    def handle_actions(self, oven):
        # checks if oven is active and powered
        if oven.is_active and oven.is_powered:
            # if oven has no pizza, reset timer and set to inactive
                if oven.held_item is None:
                    return
            # if oven has pizza that is baked and has been there too long; destroy pizza
                if oven.held_item.state == PizzaState.baked:
                    return
            # if oven has pizza that is finished baking, set pizza status to baked
                if oven.timer == TimerState.finished:
                    return
            # if oven has pizza that is still baking, subtract from timer
                if oven.timer > TimerState.finished:
                    return

   


        

              


