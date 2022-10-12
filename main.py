# 1. Define and create pokemon
# 2. Define and create basic pokemon abilities
# 3. Allow two pokemons to fight each other

from pokemon import Pokemon, PokemonType
from ability import Ability
from pokemons import *
import random

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

def battleground():
    poke_tab = []
    pc_pokedex = pokedex.copy()
    for i in range(3):
        poks = random.choice(pc_pokedex)
        poke_tab.append(poks)
        pc_pokedex.remove(poks)
    enum_poks = enumerate(pokedex)
    print('Available pokemons to add:')
    for i, pokemon in enum_poks:
        print(f'{int(i)} = {pokemon.name}')
    player_pokedex = []
    for i in range(3):
        poke_num = int(input('Choose pokemon number to add to your hand:'))
        player_pokedex.append(pokedex[poke_num])
    print('Choose pokemon to fight!')
    enum_player_pokedex = enumerate(player_pokedex)
    for i, pokemon in enum_player_pokedex:
        print(f'{int(i)} = {pokemon.name}')
    poke_start = int(input('Choose starting pokemon!:'))
    poke_player = player_pokedex[poke_start]
    player_pokedex.remove(poke_player)
    print(poke_player.name)
    poke1_pc = random.choice(poke_tab)
    poke_tab.remove(poke1_pc)
    battle_arena(poke_player, poke1_pc)
    print(poke_player.current_hp)
    print(poke1_pc.current_hp)
    if poke_player.current_hp > 0:
        poke2_pc = random.choice(poke_tab)
        battle_arena(poke_player, poke2_pc)
    if poke1_pc.current_hp > 0:
        enum_player2 = enumerate(player_pokedex)
        for i, pokemon in enum_player2:
            print(f'{int(i)} = {pokemon.name}')
        second_pok = int(input('Your pokemon lost the battle. Choose another pokemon'))
        second_pok_fight = player_pokedex[second_pok]
        battle_arena(poke1_pc, second_pok_fight)


# battleground()

print(Pokemon.create(chikorita))