import random


class Battleground():

    def get_poke_player(self, pokemon, poke_list):
        poke_list.remove(pokemon)
        self.show_pokedex(poke_list)
        new_pokemon = int(input('Choose pokemon'))
        return new_pokemon

    def get_poke_pc(self, pokemon, poke_list):
        poke_list.remove(pokemon)
        new_pokemon = random.choice(poke_list)
        return new_pokemon