from pokemon import Pokemon
from player import Player


def battle_arena(pretendent: Pokemon, champion: Pokemon) -> None:
    if pretendent.is_alive(pretendent) and champion.is_alive(champion):
        if pretendent.speed < champion.speed:
            pretendent, champion = champion, pretendent
        while pretendent.current_hp > 0 and champion.current_hp > 0:
            pretendent.attack(champion)
            if champion.current_hp > 0:
                champion.attack(pretendent)


def starting_poke_player(player: Player) -> Pokemon:
    print("Choose one starting pokemon: ")
    old_player_pokemon = player.choose_pokemon(player.game_pokedex)
    return old_player_pokemon


def starting_poke_trainer(computer: Player) -> Pokemon:
    old_pc_pokemon = computer.choose_pokemon(computer.game_pokedex)
    return old_pc_pokemon


def battleground(player: Player, computer: Player):
    old_player_pokemon = starting_poke_player(player)
    old_pc_pokemon = starting_poke_trainer(computer)
    player_score = 0
    computer_score = 0
    while player_score != 3 and computer_score != 3:
        battle_arena(old_player_pokemon, old_pc_pokemon)
        if old_player_pokemon.current_hp > 0:
            print(f"Your pokemon({old_player_pokemon.name}) wins")
            computer_score += 1
            if computer_score != 3:
                new_computer_pokemon = computer.get_poke(computer.game_pokedex)
                print("Selected computer pokemon:", new_computer_pokemon)
                old_pc_pokemon = new_computer_pokemon
        else:
            print(f"Your pokemon({old_player_pokemon.name}) lost")
            player_score += 1
            if player_score != 3:
                new_player_pokemon = player.get_poke(player.game_pokedex)
                print("Selected player pokemon:", new_player_pokemon)
                old_player_pokemon = new_player_pokemon
    if player_score == 3:
        print(f"Your pokemons lose with trainer {computer.name}. KEKW")
    else:
        print(f"Your pokemons win with trainer {computer.name}. PogU")
