from pokemons import *
from player import HumanPlayer, Trainer, PcPlayer
from battleground import battleground, battle_arena
import random
from enum import Enum


def adventure():
    print('1. Grass 2. Lavender Town 3. Cerulean Cave')
    craine = input('Choose land to adventure ')
    if craine == '1':
        computer = PcPlayer("computer")
        computer.fill_pokedex(1, grass)
    if craine == '2':
        computer = PcPlayer("computer")
        computer.fill_pokedex(1, land)
    if craine == '3':
        computer = PcPlayer("computer")
        computer.fill_pokedex(1, cave)
    if player.can_fight():
        battle_arena(player.game_pokedex[0], computer.game_pokedex[0])
        if player.can_fight():
            print(f"Your pokemons win with {computer.game_pokedex[0].name}. PogU")
        else:
            print(f"Your pokemons lose with {computer.game_pokedex[0].name}. KEKW")
        if computer.game_pokedex[0].is_alive() is False:
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
        print(f'What a beatifull adventure with {player.game_pokedex[0].name}')
    else:
        print('You have to heal your pokemons')


def fight():
    lorelei = Trainer("lorelei", [bulbasaur, bulbasaur, bulbasaur])
    bruno = Trainer("bruno", [bulbasaur, bulbasaur, bulbasaur])
    agatha = Trainer("agatha", [bulbasaur, bulbasaur, bulbasaur])

    trainers = [lorelei, bruno, agatha]

    for trainer in trainers:
        if player.can_fight():
            print(f'Now you are fighting with {trainer.name.capitalize()} !')
            battleground(player, trainer)
        else:
            break


def heal():
    hospital_decision = None
    while hospital_decision != '3':
        for index, pokemon in enumerate(player.game_pokedex):
            print(f"{index}: {pokemon.name} with {pokemon.current_hp} hp")
        ind_poke = int(input('Choose pokemon to revive or heal. '))
        hosp_poke = player.game_pokedex[ind_poke]
        hospital_decision = input('1. Revive pokemon 2. Heal pokemon 3. Quit hospital. ')
        if hospital_decision == '1':
            hosp_poke.revive()
        if hospital_decision == '2':
            hosp_poke.heal()


def quit():
    print('Goodbye')


def print_options(options):
    for key, value in options.items():
        print(key, value[0])


game_options = {1: ('Adventure', adventure), 2: ('Fight', fight), 3: ('Heal', heal), 4: ('Quit', quit)}


player = HumanPlayer("robi")
print("Choose starter pokemon:")
for index, pokemon in enumerate(grass):
    print(f"{index} = {pokemon['name']}")
player.fill_pokedex(1, grass)
print_options(game_options)
ask_player = input('Type number what u want to do. ')
while ask_player != '4':
    journey = game_options.get(int(ask_player))[1]
    journey()
    print_options(game_options)
    ask_player = input('Type number what u want to do. ')
quit()
