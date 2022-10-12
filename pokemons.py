from pokemon import Pokemon, PokemonType
from ability import Ability

razor_leaf = Ability('razor_leaf', 5)
frenzy_plant = Ability('frenzy_plant', 40)
grass_knot = Ability('grass_knot', 25)

surf = Ability('surf', 15)
hydro_cannon = Ability('hydro_cannon', 35)
water_gun = Ability('water_gun', 20)

overheat = Ability('overheat', 10)
blast_burn = Ability('blast_burn', 45)
flamethrower = Ability('flamethrower', 15)

# bulbasaur = Pokemon('bulbasaur', 25, 270, PokemonType.GRASS)
# squirtle = Pokemon('squirtle', 30, 400, PokemonType.WATER)
# charmander = Pokemon('charmander', 40, 300, PokemonType.FIRE)

bulbasaur = {'name': 'bulbasaur', 'damage': 25, 'max_hp': 270, 'type': PokemonType.GRASS, 'abilities': [razor_leaf, frenzy_plant]}
squirtle = {'name': 'squirtle', 'damage': 30, 'max_hp': 400, 'type': PokemonType.WATER, 'abilities': [surf, hydro_cannon]}
charmander = {'name': 'charmander', 'damage': 40, 'max_hp': 300, 'type': PokemonType.FIRE, 'abilities': [flamethrower, blast_burn]}

# chikorita = Pokemon('chikorita', 25, 270, PokemonType.GRASS)
# totodile = Pokemon('totodile', 30, 400, PokemonType.WATER)
# cyndaquil = Pokemon('cyndaquil', 40, 300, PokemonType.FIRE)

chikorita = {'name': 'chikorita', 'damage': 25, 'max_hp': 270, 'type': PokemonType.GRASS, 'abilities': [grass_knot, frenzy_plant]}
totodile = {'name': 'totodile', 'damage': 30, 'max_hp': 400, 'type': PokemonType.WATER, 'abilities': [water_gun, surf]}
cyndaquil = {'name': 'cyndaquil', 'damage': 40, 'max_hp': 300, 'type': PokemonType.FIRE, 'abilities': [blast_burn, overheat]}



pokedex = [bulbasaur, squirtle, charmander, chikorita, totodile, cyndaquil]
