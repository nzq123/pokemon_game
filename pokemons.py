from pokemon import PokemonType
from ability import Ability, AbilityType

razor_leaf = Ability('razor_leaf', 5, AbilityType.GRASS)
frenzy_plant = Ability('frenzy_plant', 40, AbilityType.GRASS)
grass_knot = Ability('grass_knot', 25, AbilityType.GRASS)

surf = Ability('surf', 15, AbilityType.WATER)
hydro_cannon = Ability('hydro_cannon', 35, AbilityType.WATER)
water_gun = Ability('water_gun', 20, AbilityType.WATER)

overheat = Ability('overheat', 10, AbilityType.FIRE)
blast_burn = Ability('blast_burn', 45, AbilityType.FIRE)
flamethrower = Ability('flamethrower', 15, AbilityType.FIRE)

bulbasaur = {'name': 'bulbasaur', 'damage': 49, 'max_hp': 450, 'speed': 45, 'type': [PokemonType.GRASS, PokemonType.WATER], 'abilities': [razor_leaf, frenzy_plant]}
squirtle = {'name': 'squirtle', 'damage': 48, 'max_hp': 440, 'speed': 43, 'type': [PokemonType.WATER], 'abilities': [surf, hydro_cannon]}
charmander = {'name': 'charmander', 'damage': 52, 'max_hp': 390, 'speed': 65, 'type': [PokemonType.FIRE], 'abilities': [flamethrower, blast_burn]}

chikorita = {'name': 'chikorita', 'damage': 49, 'max_hp': 450, 'speed': 45, 'type': [PokemonType.GRASS], 'abilities': [grass_knot, frenzy_plant]}
totodile = {'name': 'totodile', 'damage': 65, 'max_hp': 500, 'speed': 43, 'type': [PokemonType.WATER], 'abilities': [water_gun, surf]}
cyndaquil = {'name': 'cyndaquil', 'damage': 52, 'max_hp': 390, 'speed': 65, 'type': [PokemonType.FIRE], 'abilities': [blast_burn, overheat]}

pokedex = [bulbasaur, squirtle, charmander, chikorita, totodile, cyndaquil]
