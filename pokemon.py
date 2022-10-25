from __future__ import annotations

import random
from enum import Enum
from typing import List

from ability import Ability, AbilityType


class PokemonType(str, Enum):
    WATER = "water"
    FIRE = "fire"
    GRASS = "grass"
    ICE = "ice"
    GROUND = "ground"
    POISON = "poison"


def multi_by_type(attack_type, poke_types):
    grass = {
        PokemonType.FIRE: 0.5,
        PokemonType.WATER: 2,
        PokemonType.GRASS: 0.5,
        PokemonType.ICE: 0.5,
        PokemonType.GROUND: 2,
        PokemonType.POISON: 0.5,
    }
    water = {
        PokemonType.FIRE: 2,
        PokemonType.WATER: 0.5,
        PokemonType.GRASS: 0.5,
        PokemonType.ICE: 0.5,
        PokemonType.GROUND: 2,
        PokemonType.POISON: 1,
    }
    fire = {
        PokemonType.FIRE: 0.5,
        PokemonType.WATER: 0.5,
        PokemonType.GRASS: 2,
        PokemonType.ICE: 2,
        PokemonType.GROUND: 0.5,
        PokemonType.POISON: 1,
    }
    ice = {
        PokemonType.FIRE: 0.5,
        PokemonType.WATER: 0.5,
        PokemonType.GRASS: 2,
        PokemonType.ICE: 0.5,
        PokemonType.GROUND: 2,
        PokemonType.POISON: 1,
    }
    ground = {
        PokemonType.FIRE: 2,
        PokemonType.WATER: 1,
        PokemonType.GRASS: 1,
        PokemonType.ICE: 0.5,
        PokemonType.GROUND: 1,
        PokemonType.POISON: 2,
    }
    poison = {
        PokemonType.FIRE: 0.5,
        PokemonType.WATER: 0.5,
        PokemonType.GRASS: 2,
        PokemonType.ICE: 0.5,
        PokemonType.GROUND: 0.5,
        PokemonType.POISON: 1,
    }

    types = {
        AbilityType.GRASS: grass,
        AbilityType.WATER: water,
        AbilityType.FIRE: fire,
        AbilityType.ICE: ice,
        AbilityType.GROUND: ground,
        AbilityType.POISON: poison,
    }

    res = 1
    multi = types[attack_type]
    for i in poke_types:
        res *= multi[i]
    return res


def did_hit(attack: Ability) -> bool:
    hit_chance = attack.accuracy * 0.7
    hit_range = random.randint(0, 100)
    return hit_chance >= hit_range


def is_hit_crt(attack: Ability) -> bool:
    crt_chance = attack.accuracy / 512 * 100
    crt_range = random.randint(0, 100)
    return crt_chance >= crt_range


class Pokemon:
    def __init__(self, name: str, damage: float, max_hp: float, speed: float, type: PokemonType):
        self.name = name
        self.damage = damage
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.speed = speed
        self.type = type
        self.abilities: List[Ability] = []

    # def __init__(self):
    #     self.name = 'Bulbasaur'
    #     self.damage = 70
    #     self.max_hp = 50
    #     self.current_hp = self.max_hp
    #     self.type = None
    #     self.abilities = []

    def __str__(self) -> str:
        return f"{self.name} with {self.damage} attack and {self.current_hp} hp as {self.type} type with {self.abilities} abilities"

    def attack(self, other: Pokemon) -> None:
        attack = random.choice(self.abilities)
        crt_attack = is_hit_crt(attack)
        if did_hit(attack):
            champ_dmg = (self.damage + attack.damage) * multi_by_type(attack.type, other.type)
            for i in self.type:
                if i == attack.type:
                    champ_dmg *= 1.5
            if crt_attack:
                champ_dmg *= 2
            champ_dmg = round(champ_dmg, 3)
            other.current_hp = other.current_hp - champ_dmg
            other.current_hp = max(other.current_hp, 0)
            other.current_hp = round(other.current_hp, 3)
            if crt_attack:
                print(
                    f"Attack from {self.name} ({attack.name}) was critical hit for {champ_dmg} dmg. {other.name} is left with {other.current_hp} hp"
                )
            else:
                print(
                    f"Attack from {self.name} ({attack.name}) was hit for {champ_dmg} dmg. {other.name} is left with {other.current_hp} hp"
                )
        else:
            print(f"Attack from {self.name} was missed. {other.name} is left with {other.current_hp} hp")

    def learn(self, ability: Ability) -> None:
        self.abilities.append(ability)

    def is_alive(self, pokemon: Pokemon) -> bool:
        return pokemon.current_hp > 0

    @classmethod
    def create(cls, settings) -> Pokemon:
        new_pokemon = Pokemon(
            settings.get("name"),
            settings.get("damage"),
            settings.get("max_hp"),
            settings.get("speed"),
            settings.get("type"),
        )
        poke_abilities = settings.get("abilities")
        for ability in poke_abilities:
            new_pokemon.learn(ability)
        return new_pokemon
