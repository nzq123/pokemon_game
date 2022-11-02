import random
from abc import ABC, abstractmethod
from typing import List, Optional

from pokemon import Pokemon
from pokemons import grass


class Player(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.game_pokedex: List[Pokemon] = []

    def show_pokedex(self, poke_list: List[Pokemon]) -> None:
        for index, pokemon in enumerate(poke_list):
            print(f"{index} = {pokemon.name}")

    @abstractmethod
    def choose_pokemon(self) -> Optional[Pokemon]:
        pass

    @abstractmethod
    def fill_pokedex(self, num, pokedex) -> None:
        pass

    def can_fight(self) -> bool:
        for pokemon in self.game_pokedex:
            if pokemon.is_alive():
                return True
        return False


class HumanPlayer(Player):
    def choose_pokemon(self) -> Optional[Pokemon]:
        alive_pokemons = []
        for pokemon in self.game_pokedex:
            if pokemon.is_alive():
                alive_pokemons.append(pokemon)
        self.show_pokedex(alive_pokemons)
        if len(alive_pokemons) != 0:
            new_pokemon = int(input("Choose pokemon: "))
            return alive_pokemons[new_pokemon]

    def fill_pokedex(self, num, pokedex) -> None:
        for i in range(num):
            poke_num = int(input("Choose pokemon number to add to your hand: "))
            self.game_pokedex.append(Pokemon.create(pokedex[poke_num]))


class PcPlayer(Player):
    def choose_pokemon(self) -> Optional[Pokemon]:
        alive_pokemons = []
        for pokemon in self.game_pokedex:
            if pokemon.is_alive():
                alive_pokemons.append(pokemon)
        new_pokemon = random.choice(alive_pokemons)
        return new_pokemon

    def fill_pokedex(self, num, pokedex) -> None:
        for i in range(num):
            pc_pok = random.choice(pokedex)
            self.game_pokedex.append(Pokemon.create(pc_pok))


class Trainer(Player):
    def __init__(self, name: str, poke_tab: List[dict]):
        super().__init__(name)

        for i in range(len(poke_tab)):
            pc_pok = poke_tab[i]
            self.game_pokedex.append(Pokemon.create(pc_pok))

    def choose_pokemon(self) -> Optional[Pokemon]:
        for pokemon in self.game_pokedex:
            if pokemon.is_alive():
                return pokemon

    def fill_pokedex(self, num, pokedex) -> None:
        pass
