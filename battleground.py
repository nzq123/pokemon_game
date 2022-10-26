from pokemon import Pokemon
from player import Player


def battle_arena(pretendent: Pokemon, champion: Pokemon) -> None:
    if pretendent.is_alive() and champion.is_alive():
        if pretendent.speed < champion.speed:
            pretendent, champion = champion, pretendent
        while pretendent.is_alive() and champion.is_alive():
            pretendent.attack(champion)
            if champion.is_alive():
                champion.attack(pretendent)


def battleground(player: Player, computer: Player):
    print("Choose one starting pokemon: ")
    old_player_pokemon = player.choose_pokemon()
    old_pc_pokemon = computer.choose_pokemon()
    player_score = 0
    computer_score = 0
    while player_score != 3 and computer_score != 3:
        if old_player_pokemon is None or old_pc_pokemon is None:
            break
        battle_arena(old_player_pokemon, old_pc_pokemon)
        if old_player_pokemon.is_alive():
            print(f"Your pokemon({old_player_pokemon.name}) wins")
            computer_score += 1
            if computer_score != 3:
                new_computer_pokemon = computer.choose_pokemon()
                old_pc_pokemon = new_computer_pokemon
        else:
            print(f"Your pokemon({old_player_pokemon.name}) lost")
            player_score += 1
            if player_score != 3:
                new_player_pokemon = player.choose_pokemon()
                old_player_pokemon = new_player_pokemon
    if player_score == 3:
        print(f"Your pokemons lose with trainer {computer.name}. KEKW")
    else:
        print(f"Your pokemons win with trainer {computer.name}. PogU")
