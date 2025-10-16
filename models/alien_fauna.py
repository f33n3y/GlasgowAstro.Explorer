from models.alien_life import AlienLife


class AlienFauna(AlienLife):
    def __init__(self, name: str, rarity: int):
        super().__init__(name, rarity)
