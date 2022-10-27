from pokemons import *
from player import HumanPlayer, Trainer, PcPlayer
from battleground import battleground, battle_arena
import random


player = HumanPlayer("robi")

print('1. Adventure \n2. Fighting with trainers \n3. Go sleep')
ask_player = input('Type number what u want to do. ')
if ask_player == '1':
    print("Choose starter pokemon:")
    for index, pokemon in enumerate(pokedex):
        print(f"{index} = {pokemon['name']}")
    player.fill_pokedex(1)
    computer = PcPlayer("computer")
    computer.fill_pokedex(1)
    battle_arena(player.game_pokedex[0], computer.game_pokedex[0])
    if player.can_fight():
        print(f"Your pokemons win with {computer.game_pokedex[0].name}. PogU")
    else:
        print(f"Your pokemons lose with {computer.game_pokedex[0].name}. KEKW")
    if computer.game_pokedex[0].current_hp == 0:
        decision = input('1. Catch 2. Run ')
        if decision == '1':
            for i in range(3):
                catch = random.randrange(0, 10)
                if catch < 5:
                    print(f"You catched wild {computer.game_pokedex[0].name}")
                    player.game_pokedex.append(computer.game_pokedex[0])
                    break
                else:
                    print(f"Wild {computer.game_pokedex[0].name} flies")
        else:
            print(f'You escaped after battle!')
    for pokemon in player.game_pokedex:
        print(pokemon.name)
    print(f'What a beatifull adventure with {player.game_pokedex[0].name}')
if ask_player == '2':

    print("Choose 3 starting pokemons:")

    for index, pokemon in enumerate(pokedex):
        print(f"{index} = {pokemon['name']}")

    lorelei = Trainer("lorelei", [bulbasaur, bulbasaur, bulbasaur])
    bruno = Trainer("bruno", [bulbasaur, bulbasaur, bulbasaur])
    agatha = Trainer("agatha", [bulbasaur, bulbasaur, bulbasaur])

    trainers = [lorelei, bruno, agatha]

    player.fill_pokedex(3)

    for trainer in trainers:
        if player.can_fight():
            print(f'Now you are fighting with {trainer.name.capitalize()} !')
            battleground(player, trainer)
        else:
            break
if ask_player == '3':
    print('Goodbye')