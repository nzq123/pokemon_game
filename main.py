from pokemons import *
from pokemon import Pokemon
from player import PcPlayer, HumanPlayer, Trainer
from battleground import *


print('Choose 3 starting pokemons:')

for index, pokemon in enumerate(pokedex):
    print(f"{index} = {pokemon['name']}")

player = HumanPlayer('robi')
lorelei = Trainer('lorelei', [bulbasaur, bulbasaur, bulbasaur])
bruno = Trainer('bruno', [bulbasaur, bulbasaur, bulbasaur])
agatha = Trainer('agatha', [charmander, charmander, charmander])


player.fill_pokedex()
lorelei.fill_pokedex()

a = starting_poke_player(player)
b = starting_poke_comp(lorelei)
battle_arena(a, b)
battleground(player, lorelei, a, b)
if len(lorelei.game_pokedex) == 0:
    lorelei = bruno
    bruno.fill_pokedex()
    b = starting_poke_comp(bruno)
    battleground(player, bruno, a, b)
    battle_arena(a, b)
    if len(bruno.game_pokedex) == 0:
        bruno = agatha
        agatha.fill_pokedex()
        b = starting_poke_comp(agatha)
        battleground(player, agatha, a, b)
        battle_arena(a, b)

