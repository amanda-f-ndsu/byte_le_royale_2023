from game.common.action import Action
from game.common.cook import Cook
from game.common.game_object import GameObject
from game.common.enums import *


class Player(GameObject):
    def __init__(self, code=None, team_name=None, action=None, cook=None):
        super().__init__()
        self.object_type = ObjectType.player
        
        self.functional = True
        self.error = None
        self.team_name = team_name
        self.cook_skin = "white"
        self.code = code
        self.action = action
        self.cook = cook

    @property
    def action(self) -> Action:
        return self.__action

    @action.setter
    def action(self, action: Action):
        if isinstance(action, Action) or action is None:
            self.__action = action

    def to_json(self):
        data = super().to_json()

        data['functional'] = self.functional
        data['error'] = self.error
        data['team_name'] = self.team_name
        data['cook_skin'] = self.cook_skin
        data['action'] = self.action.to_json() if self.action else None
        data['cook'] = self.cook.to_json() if self.cook else None

        return data

    def from_json(self, data):
        super().from_json(data)
        
        self.functional = data['functional']
        self.error = data['error']
        self.team_name = data['team_name']
        self.cook_skin = data['cook_skin']
        act = Action()
        self.action = act.from_json(data['action']) if data['action'] else None
        ck = Cook()
        self.cook = ck.from_json(data['cook']) if data['cook'] else None

    def __str__(self):
        p = f"""ID: {self.id}
            Team name: {self.team_name}
            Action: {self.action}
            """
        return p
