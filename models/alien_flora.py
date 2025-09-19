class AlienFlora:
    def __init__(self, name: str, rarity: int):
        self.name = name
        self.rarity = rarity

    def describe(self):
        return f"{self.__class__.__name__}: ({self.name}, {self.rarity})"
