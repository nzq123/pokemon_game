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
        print()
        print(f'{pretendent.name} won that battle with {pretendent.current_hp} hp.')
        print()
    else:
        print()
        print(f'{champion.name} won that battle with {champion.current_hp} hp.')
        print()

def battleground():
    print('Choose 3 starting pokemons:')

    for index, pokemon in enumerate(pokedex):
        print(f"{index} = {pokemon['name']}")

    player_game_pokedex = []
    for i in range(3):
        poke_num = int(input('Choose pokemon number to add to your hand: '))
        player_game_pokedex.append(Pokemon.create(pokedex[poke_num]))

    pc_game_pokedex = []
    for i in range(3):
        pc_pok = random.choice(pokedex)
        pc_game_pokedex.append(Pokemon.create(pc_pok))

    print('Available pokemons to fight')
    for index, pokemon in enumerate(player_game_pokedex):
        print(f"{index} = {pokemon.name}")
    first = int(input('Choose 1st pokemon to fight: '))

    first_player_poke = player_game_pokedex[first]
    first_pc_poke = random.choice(pc_game_pokedex)

    while len(pc_game_pokedex) > 0 and len(player_game_pokedex) > 0:

        battle_arena(first_player_poke, first_pc_poke)

        if first_player_poke.current_hp > 0:
            pc_game_pokedex.remove(first_pc_poke)
            second_pc_poke = random.choice(pc_game_pokedex)
            battle_arena(second_pc_poke, first_player_poke)

        if first_pc_poke.current_hp > 0:
            player_game_pokedex.remove(first_player_poke)
            for i, pokemon in enumerate(player_game_pokedex):
                print(f'{i} = {pokemon.name}')
            second = int(input('Your pokemon lost the battle. Choose another pokemon'))
            second_player_poke = player_game_pokedex[second]
            battle_arena(second_player_poke, first_pc_poke)




battleground()
