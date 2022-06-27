from game.common.items.item import Item
from game.common.enums import *

class Topping(Item):

    def __init__(self, worth: int, quality: float = 0, topping_type: ToppingType = ToppingType.none, is_cut: bool=False):
        super().__init__(worth, quality)
        self.object_type = ObjectType.topping
        self.topping_type = topping_type
        self.is_cut = is_cut

    @property
    def topping_type(self) -> ToppingType:
        return self.__topping_type

    @property
    def is_cut(self) -> bool:
        return self.__is_cut

    @topping_type.setter
    def topping_type(self, topping_type: ToppingType):
        self.__topping_type = topping_type

    @is_cut.setter
    def is_cut(self, is_cut: bool):
        self.__is_cut = is_cut

    def to_json(self):
        data = super().to_json()
        data['topping_type'] = self.topping_type
        data['is_cut'] = self.is_cut
        return data

    def from_json(self, data: dict) -> 'Topping':
        super().from_json(data)
        self.topping_type = data['topping_type']
        self.is_cut = data['is_cut']
