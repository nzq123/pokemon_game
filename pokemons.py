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

bulbasaur = {'name': 'bulbasaur', 'damage': 25, 'max_hp': 270, 'type': [PokemonType.GRASS, PokemonType.WATER], 'abilities': [razor_leaf, frenzy_plant]}
squirtle = {'name': 'squirtle', 'damage': 30, 'max_hp': 400, 'type': PokemonType.WATER, 'abilities': [surf, hydro_cannon]}
charmander = {'name': 'charmander', 'damage': 40, 'max_hp': 300, 'type': PokemonType.FIRE, 'abilities': [flamethrower, blast_burn]}

chikorita = {'name': 'chikorita', 'damage': 25, 'max_hp': 270, 'type': PokemonType.GRASS, 'abilities': [grass_knot, frenzy_plant]}
totodile = {'name': 'totodile', 'damage': 30, 'max_hp': 400, 'type': PokemonType.WATER, 'abilities': [water_gun, surf]}
cyndaquil = {'name': 'cyndaquil', 'damage': 40, 'max_hp': 300, 'type': PokemonType.FIRE, 'abilities': [blast_burn, overheat]}

pokedex = [bulbasaur, squirtle, charmander, chikorita, totodile, cyndaquil]
