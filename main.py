from pokemons import *
from player import HumanPlayer, Trainer
from battleground import battleground


print('1. Adventure \n2. Fighting with trainers')
ask_player = input('Type number what u want to do. ')
if ask_player == '1':
    print('What a beatifull adventure!')
if ask_player == '2':

    print("Choose 3 starting pokemons:")

    for index, pokemon in enumerate(pokedex):
        print(f"{index} = {pokemon['name']}")

    player = HumanPlayer("robi")
    lorelei = Trainer("lorelei", [bulbasaur, bulbasaur, bulbasaur])
    bruno = Trainer("bruno", [bulbasaur, bulbasaur, bulbasaur])
    agatha = Trainer("agatha", [bulbasaur, bulbasaur, bulbasaur])

    trainers = [lorelei, bruno, agatha]

    player.fill_pokedex()

    for trainer in trainers:
        if player.can_fight():
            print(f'Now you are fighting with {trainer.name.capitalize()} !')
            battleground(player, trainer)
        else:
            break