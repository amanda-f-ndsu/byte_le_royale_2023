from game.common.enums import ObjectType
from game.common.game_object import GameObject


class Tile(GameObject):

    def __init__(self, stored_object: GameObject):
        super().__init__()
        self.object_type = ObjectType.tile
        self.stored_object = stored_object if isinstance(Station) or isinstance(Dispenser) else None



    @property
    def stored_object(self) -> GameObject:
        return self.__stored_object

    @stored_object.setter
    def stored_object(self, stored_object: GameObject):
        self.__stored_object = stored_object if isinstance(Station) or isinstance(Dispenser) else None


    def to_json(self):
        data = super().to_json()
        data['stored_object'] = self.stored_object
        return data

    def from_json(self, data: dict) -> 'Tile':
        super().from_json(data)
        self.stored_object = data['stored_object']
        return self