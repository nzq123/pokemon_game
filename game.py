from pokemons import *
from pokemon import Pokemon
from player import HumanPlayer, Trainer, PcPlayer
from battleground import battleground, battle_arena
import random
import sys


def adventure(player):
    print('1. Grass 2. Lavender Town 3. Cerulean Cave')
    land = input('Choose land to adventure ')
    if land == '1':
        pokemon = select_random_pokemon(grass)
    if land == '2':
        pokemon = select_random_pokemon(lake)
    if land == '3':
        pokemon = select_random_pokemon(cave)
    if player.can_fight():
        battle_arena(player.game_pokedex[0], pokemon)
        if player.can_fight():
            print(f"Your pokemons win with {pokemon.name}. PogU")
        else:
            print(f"Your pokemons lose with {pokemon.name}. KEKW")
        if pokemon.is_alive() is False:
            decision = input('1. Catch 2. Run ')
            if decision == '1':
                for i in range(3):
                    catch = random.randrange(0, 10)
                    if catch < 5:
                        print(f"You catched wild {pokemon.name}")
                        player.game_pokedex.append(pokemon)
                        break
                    else:
                        print(f"Wild {pokemon} flies")
            else:
                print(f'You escaped after battle!')
        print(f'What a beatifull adventure with {player.game_pokedex[0].name}')
    else:
        print('You have to heal your pokemons')


def fight(player):
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


def heal(player):
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


def quit(player):
    print('Goodbye')
    sys.exit(0)


def print_options(options):
    for key, value in options.items():
        print(key, value[0])


def select_pokemon(pokedex):
    poke_num = int(input("Choose pokemon number to add to your hand: "))
    return Pokemon.create(pokedex[poke_num])


def select_random_pokemon(pokedex):
    pc_pok = random.choice(pokedex)
    return Pokemon.create(pc_pok)


game_options = {1: ('Adventure', adventure), 2: ('Fight', fight), 3: ('Heal', heal), 4: ('Quit', quit)}


class Game:
    def __init__(self, player):
        self.player = player

    def play(self):
        print("Choose starter pokemon:")
        for index, pokemon in enumerate(grass):
            print(f"{index} = {pokemon['name']}")
        poke = select_pokemon(grass)
        self.player.get_pokemon(poke)
        while True:
            print_options(game_options)
            ask_player = input('Type number what u want to do. ')
            action = game_options.get(int(ask_player))[1]
            action(self.player)