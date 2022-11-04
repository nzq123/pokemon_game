from pokemon import Pokemon
from player import Player, HumanPlayer


def battle_arena(pretendent: Pokemon, champion: Pokemon) -> None:
    if pretendent.is_alive() and champion.is_alive():
        if pretendent.speed < champion.speed:
            pretendent, champion = champion, pretendent
        while pretendent.is_alive() and champion.is_alive():
            pretendent.attack(champion)
            if champion.is_alive():
                champion.attack(pretendent)


def battleground(player: HumanPlayer, computer: Player):
    print("Choose one starting pokemon: ")
    old_player_pokemon = player.choose_pokemon()
    old_player_pokemon.trainer = player
    old_pc_pokemon = computer.choose_pokemon()
    while player.can_fight() and computer.can_fight():
        battle_arena(old_player_pokemon, old_pc_pokemon)
        if old_player_pokemon.is_alive():
            print(f"Your pokemon({old_player_pokemon.name}) wins")
            new_computer_pokemon = computer.choose_pokemon()
            old_pc_pokemon = new_computer_pokemon
        else:
            print(f"Your pokemon({old_player_pokemon.name}) lost")
            new_player_pokemon = player.choose_pokemon()
            old_player_pokemon = new_player_pokemon
            if player.can_fight():
                old_player_pokemon.trainer = player
    if player.can_fight():
        print(f"Your pokemons win with {computer.name}. PogU")
    else:
        print(f"Your pokemons lose with {computer.name}. KEKW")
