from dataclasses import dataclass

@dataclass(frozen=True)
class Discovery:
    """
    Represents a single unique discovery of alien life.
    Immutable and hashable, so it can be stored in a set.
    """
    name: str
    type_of_life: str
    x: int
    y: int
    rarity: int
