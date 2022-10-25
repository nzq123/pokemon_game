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

trainers = [lorelei, bruno, agatha]

player.fill_pokedex()


for i in range(len(trainers)):
    battleground(player, trainers[i])


