from enum import Enum


class AbilityType(str, Enum):
    WATER = 'water'
    FIRE = 'fire'
    GRASS = 'grass'
    ICE = 'ice'
    GROUND = 'ground'
    POISON = 'poison'


class Ability:
    def __init__(self, name: str, damage: float, accuracy: int, type: AbilityType, cooldown: int) -> None:
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.type = type
        self.cooldown = cooldown

    def __str__(self) -> str:
        return f'{self.name} with {self.damage} damage'

    def __repr__(self) -> str:
        return f'{self.name} with {self.damage} damage'


