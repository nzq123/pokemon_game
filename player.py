from abc import ABC, abstractmethod
from pokemons import *
import random


class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.game_pokedex = []

    def show_pokedex(self, poke_list):
        for index, pokemon in enumerate(poke_list):
            print(f'{index} = {pokemon.name}')

    @abstractmethod
    def choose_pokemon(self, poke_list):
        pass

    def get_poke(self, poke_list):
        new_pokemon = self.choose_pokemon(poke_list)
        return new_pokemon

    def remove_poke(self, pokemon, poke_list):
        poke_list.remove(pokemon)

    @abstractmethod
    def fill_pokedex(self):
        pass


class HumanPlayer(Player):
    def choose_pokemon(self, poke_list):
        self.show_pokedex(poke_list)
        new_pokemon = int(input('Choose pokemon: '))
        return poke_list[new_pokemon]

    def fill_pokedex(self):
        for i in range(3):
            poke_num = int(input('Choose pokemon number to add to your hand: '))
            self.game_pokedex.append(Pokemon.create(pokedex[poke_num]))


class PcPlayer(Player):
    def choose_pokemon(self, poke_list):
        new_pokemon = random.choice(poke_list)
        return new_pokemon

    def fill_pokedex(self):
        for i in range(3):
            pc_pok = random.choice(pokedex)
            self.game_pokedex.append(Pokemon.create(pc_pok))



