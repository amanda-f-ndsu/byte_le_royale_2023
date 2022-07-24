from game.common.game_object import GameObject
from game.common.enums import ObjectType
from game.common.items.item import Item
from game.common.items.pizza import Pizza
from game.common.items.topping import Topping


class Dispenser(GameObject):

    def __init__(self):
        super().__init__()
        self.object_type: ObjectType = ObjectType.dispenser
        self.item_stored: GameObject = GameObject()

    @property
    def item_stored(self) -> GameObject:
        return self.__item_stored

    @item_stored.setter
    def item_stored(self, item_stored: GameObject):
        self.__item_stored = item_stored

    def dispense(self):
        pass

    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['item_stored'] = self.item_stored.to_json() if self.item_stored else None
        return dict_data

    def from_json(self, data: dict) -> 'Dispenser':
        super().from_json(data)
        temp: Item = data['item_stored']
        if not temp:
            self.item_stored = None
        elif temp.object_type == ObjectType.pizza:
            self.item_stored = Pizza().from_json(data['item_stored'])
        else:
            self.item_stored = Topping().from_json(data['item_stored'])
        return self

    def obfuscate(self) -> None:
        super().obfuscate()
        pass
