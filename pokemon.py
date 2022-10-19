from enum import Enum
import random


class PokemonType(str, Enum):
    WATER = 'water'
    FIRE = 'fire'
    GRASS = 'grass'


def multi_by_type(first, second):
    if first == PokemonType.WATER:
        if second == PokemonType.FIRE:
            return 1.5
        elif second == PokemonType.WATER:
            return 1
        elif second == PokemonType.GRASS:
            return 0.5
    if first == PokemonType.GRASS:
        if second == PokemonType.WATER:
            return 1.5
        elif second == PokemonType.GRASS:
            return 1
        elif second == PokemonType.FIRE:
            return 0.5
    if first == PokemonType.FIRE:
        if second == PokemonType.GRASS:
            return 1.5
        elif second == PokemonType.FIRE:
            return 1
        elif second == PokemonType.WATER:
            return 0.5


class Pokemon:

    def __init__(self, name, damage, max_hp, type):
        self.name = name
        self.damage = damage
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.type = type
        self.abilities = []

    # def __init__(self):
    #     self.name = 'Bulbasaur'
    #     self.damage = 70
    #     self.max_hp = 50
    #     self.current_hp = self.max_hp
    #     self.type = None
    #     self.abilities = []

    def __str__(self):
        return f'{self.name} with {self.damage} attack and {self.current_hp} hp as {self.type} type with {self.abilities} abilities'

    def attack(self, other):
        attack = random.choice(self.abilities)
        if self.hit_chance():
            champ_dmg = round(((self.damage + attack.damage) * 0.7) * multi_by_type(self.type, other.type), 3)
            if self.type == attack.type:
                champ_dmg *= 1.5
            other.current_hp = other.current_hp - champ_dmg
            other.current_hp = max(other.current_hp, 0)
            print(f'Attack from {self.name} ({attack.name}) was hit for {champ_dmg} dmg. {other.name} is left with {other.current_hp} hp')
        else:
            print(f'Attack from {self.name} was missed. {other.name} is left with {other.current_hp} hp')

    def heal(self):
        if self.current_hp + 10 > self.max_hp:
            self.current_hp = self.max_hp
        else:
            self.current_hp += 10
        print(f'{self.name} was healed to {self.current_hp} hp')

    def train(self):
        self.damage += 5
        self.current_hp += 5
        self.max_hp += 5
        print(f'{self.name} was trained and now has {self.damage} damage and {self.current_hp} out of {self.max_hp} hp')

    def learn(self, ability):
        self.abilities.append(ability)

    def is_alive(self, pokemon):
        return pokemon.current_hp > 0

    @staticmethod
    def hit_chance():
        tab = [1, 2, 3, 4]
        chance = random.choice(tab)
        return chance < 4

    @classmethod
    def create(cls, settings):
        new_pokemon = Pokemon(settings.get('name'), settings.get('damage'), settings.get('max_hp'), settings.get('type'))
        poke_abilities = settings.get('abilities')
        for ability in poke_abilities:
            new_pokemon.learn(ability)
        return new_pokemon








