from game.common.enums import ObjectType
from game.common.game_object import GameObject


class Item(GameObject):

    def __init__(self, quality: int, value: int):
        super().__init__()
        self.object_type = ObjectType.item
        self.quality = quality if quality >= 1 else 0
        self.value = value if value >= 1 else 0

    @property
    def quality(self) -> int:
        return self.__quality

    @property
    def value(self) -> int:
        return self.__value

    @quality.setter
    def quality(self, quality: int):
        self.__quality = quality if quality >= 1 else 0

    @value.setter
    def value(self, value: int):
        self.__value = value if value >= 1 else 0

    def to_json(self):
        data = super().to_json()
        data['quality'] = self.quality
        data['value'] = self.value
        return data

    def from_json(self, data: dict) -> 'Item':
        super().from_json(data)
        self.quality = data['quality']
        self.value = data['value']
        return self

