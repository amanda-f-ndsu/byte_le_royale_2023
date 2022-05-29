from game.common.game_object import GameObject

class Dispenser(GameObject):

    def __init__(self):
        super().__init__()
        self.go_item_stored = None

    def dispense(self):
        pass

    def to_json(self) -> dict:
        dict_data = super().to_json()
        dict_data['go_item_stored'] = self.go_item_stored
        return dict_data

    def from_json(self, dict_data:dict) -> 'Dispenser':
        super().from_json(dict_data)
        self.go_item_stored = dict_data['go_item_stored']

        return self

    def obfuscate(self) -> None:
        super().obfuscate()
        pass