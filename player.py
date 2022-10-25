from abc import ABC, abstractmethod
from pokemons import *
from pokemon import Pokemon
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
        alive_pokemons = []
        for pokemon in poke_list:
            if pokemon.current_hp > 0:
                alive_pokemons.append(pokemon)
        self.show_pokedex(alive_pokemons)
        new_pokemon = int(input('Choose pokemon: '))
        return alive_pokemons[new_pokemon]

    def fill_pokedex(self):
        for i in range(3):
            poke_num = int(input('Choose pokemon number to add to your hand: '))
            self.game_pokedex.append(Pokemon.create(pokedex[poke_num]))


class PcPlayer(Player):
    def choose_pokemon(self, poke_list):
        alive_pokemons = []
        for pokemon in poke_list:
            if pokemon.current_hp > 0:
                alive_pokemons.append(pokemon)
        new_pokemon = random.choice(alive_pokemons)
        return new_pokemon

    def fill_pokedex(self):
        for i in range(3):
            pc_pok = random.choice(pokedex)
            self.game_pokedex.append(Pokemon.create(pc_pok))


class Trainer(Player):
    def __init__(self, name, poke_tab):
        super().__init__(name)

        for i in range(len(poke_tab)):
            pc_pok = poke_tab[i]
            self.game_pokedex.append(Pokemon.create(pc_pok))

    def choose_pokemon(self, poke_list):
        for pokemon in poke_list:
            if pokemon.current_hp > 0:
                return pokemon

    def fill_pokedex(self):
        pass

