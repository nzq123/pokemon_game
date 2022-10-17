from abc import ABC, abstractmethod
import random


class Player(ABC):
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


class HumanPlayer(Player):
    def choose_pokemon(self, poke_list):
        self.show_pokedex(poke_list)
        new_pokemon = int(input('Choose pokemon'))
        return poke_list[new_pokemon]


class PcPlayer(Player):
    def choose_pokemon(self, poke_list):
        new_pokemon = random.choice(poke_list)
        return new_pokemon



