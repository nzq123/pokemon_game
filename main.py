# 1. Define and create pokemon
# 2. Define and create basic pokemon abilities
# 3. Allow two pokemons to fight each other

from pokemon import Pokemon, PokemonType
from ability import Ability
import random

bulbasaur = Pokemon('bulbasaur', 25, 270, PokemonType.GRASS)
squirtle = Pokemon('squirtle', 30, 400, PokemonType.WATER)
charmander = Pokemon('charmander', 40, 300, PokemonType.FIRE)

razor_leaf = Ability('razor_leaf', 5)
frenzy_plant = Ability('frenzy_plant', 40)

surf = Ability('surf', 10)
hydro_cannon = Ability('hydro_cannon', 30)

overheat = Ability('overheat', 90)
blast_burn = Ability('blast_burn', 110)

bulbasaur.learn(razor_leaf)
bulbasaur.learn(frenzy_plant)

squirtle.learn(surf)
squirtle.learn(hydro_cannon)


def battle_arena(pretendent: Pokemon, champion: Pokemon):
    while pretendent.current_hp > 0 and champion.current_hp > 0:
        pretendent.attack(champion)
        if champion.current_hp > 0:
            champion.attack(pretendent)
    # print(f"{pretendent.name if pretendent.current_hp > 0 else champion.name} is the winner!")
    if pretendent.current_hp > 0:
        print(f'{pretendent.name} won that battle with {pretendent.current_hp} hp.')
    else:
        print(f'{champion.name} won that battle with {champion.current_hp} hp.')


battle_arena(bulbasaur,squirtle)
