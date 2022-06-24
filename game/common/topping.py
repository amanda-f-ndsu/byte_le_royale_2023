from game.common.items.item import Item
from game.common.enums import *

class Topping(Item):

    def __init__(self, worth: int, quality: float = 0, topping_type: int = 0, is_cut: bool=False):
        super().__init__(self, worth, quality)
        self.topping_type = topping_type
        self.is_cut = is_cut

    @property
    def topping_type(self) -> ToppingType:
        return self.__topping_type

    @property
    def is_cut(self) -> bool:
        return self.__is_cut

    @property
    def score(self) -> int:
        if self.__topping_type == 2:
            return 20
        elif self.__topping_type == 3 or self.__topping_type == 4 or self.__topping_type == 5 \
                or self.__topping_type == 6 or self.__topping_type == 8:
            return 40
        elif self.__topping_type == 7 or self.__topping_type == 9 or self.__topping_type == 10:
            return 50
        else:
            return 0

    @topping_type.setter
    def topping_type(self, topping_type: int):
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
