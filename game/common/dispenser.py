from game.common.game_object import GameObject
from game.common.enums import ObjectType

class Dispenser(GameObject):

    def __init__(self):
        super().__init__()
        self.object_type = ObjectType.dispenser
        self.item_stored: GameObject = None

    @property
    def item_stored(self) -> GameObject:
        return self.__item_stored

    @property.setter
    def item_stored(self, item_stored: GameObject):
        self.__item_stored = item_stored


    def dispense(self):
        pass


    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['item_stored'] = self.item_stored
        return dict_data

    def from_json(self, data: dict) -> 'Dispenser':
        super().from_json(data)
        self.item_stored = data['item_stored']

    def obfuscate(self) -> None:
        super().obfuscate()
        pass
