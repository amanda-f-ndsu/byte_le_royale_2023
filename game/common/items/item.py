from game.common.enums import ObjectType
from game.common.game_object import GameObject


class Item(GameObject):

    def __init__(self, worth: int, quality: float = 0):
        super().__init__()
        self.object_type = ObjectType.item
        self.worth = worth
        self.quality = quality

    @property
    def quality(self) -> float:
        return self.__quality

    @property
    def worth(self) -> int:
        return self.__worth

    @quality.setter
    def quality(self, quality: float):
        if quality > 1:
            self.__quality = 1
        elif quality < 0:
            self.__quality = 0
        else:
            self.__quality = quality

    @worth.setter
    def worth(self, worth: int):
        self.__worth = worth

    def to_json(self):
        data = super().to_json()
        data['quality'] = self.quality
        data['worth'] = self.worth
        return data

    def from_json(self, data: dict) -> 'Item':
        super().from_json(data)
        self.quality = data['quality']
        self.worth = data['worth']
        return self

