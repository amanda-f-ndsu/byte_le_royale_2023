from game.common.enums import ObjectType
from game.common.game_object import GameObject


class Counter(GameObject):
    def __init__(self):
        super().__init__()
        self.object_type = ObjectType.counter

    def to_json(self):
        data = super().to_json()
        return data

    def from_json(self, data):
        super().from_json(data)
        return self
        