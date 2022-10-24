from pokemon import Pokemon
from player import Player


def battle_arena(pretendent: Pokemon, champion: Pokemon):
    if pretendent.speed < champion.speed:
        pretendent, champion = champion, pretendent
    while pretendent.current_hp > 0 and champion.current_hp > 0:
        pretendent.attack(champion)
        if champion.current_hp > 0:
            champion.attack(pretendent)
    # print(f"{pretendent.name if pretendent.current_hp > 0 else champion.name} is the winner!")
    # if pretendent.current_hp > 0:
    #     print()
    #     print(f'{pretendent.name} won that battle with {pretendent.current_hp} hp.')
    #     print()
    # else:
    #     print()
    #     print(f'{champion.name} won that battle with {champion.current_hp} hp.')
    #     print()


def starting_poke_player(player):
    print('Choose one starting pokemon: ')
    old_player_pokemon = player.choose_pokemon(player.game_pokedex)
    return old_player_pokemon


def starting_poke_comp(computer):
    old_pc_pokemon = computer.choose_pokemon(computer.game_pokedex)
    return old_pc_pokemon


def battleground(player, computer, old_player_pokemon, old_pc_pokemon):
    while len(player.game_pokedex) != 0 and len(computer.game_pokedex) != 0:
        if old_player_pokemon.current_hp > 0:
            print(f'Your pokemon({old_player_pokemon.name}) wins')
            computer.remove_poke(old_pc_pokemon, computer.game_pokedex)
            if len(computer.game_pokedex) != 0:
                new_computer_pokemon = computer.get_poke(computer.game_pokedex)
            battle_arena(new_computer_pokemon, old_player_pokemon)
            old_pc_pokemon = new_computer_pokemon
        else:
            print(f'Your pokemon({old_player_pokemon.name}) lost')
            print(player.game_pokedex)
            player.remove_poke(old_player_pokemon, player.game_pokedex)
            print(player.game_pokedex)
            if len(player.game_pokedex) != 0:
                new_player_pokemon = player.get_poke(player.game_pokedex)
            battle_arena(new_player_pokemon, old_pc_pokemon)
            old_player_pokemon = new_player_pokemon
    if len(player.game_pokedex) == 0:
        print(f'Your pokemons lose with trainer {computer.name}. KEKW')
    else:
        print(f'Your pokemons win with trainer {computer.name}. PogU')