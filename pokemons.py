from pokemon import Pokemon, PokemonType
from ability import Ability


bulbasaur = Pokemon('bulbasaur', 25, 270, PokemonType.GRASS)
squirtle = Pokemon('squirtle', 30, 400, PokemonType.WATER)
charmander = Pokemon('charmander', 40, 300, PokemonType.FIRE)

chikorita = Pokemon('chikorita', 25, 270, PokemonType.GRASS)
totodile = Pokemon('totodile', 30, 400, PokemonType.WATER)
cyndaquil = Pokemon('cyndaquil', 40, 300, PokemonType.FIRE)

razor_leaf = Ability('razor_leaf', 5)
frenzy_plant = Ability('frenzy_plant', 40)
grass_knot = Ability('grass_knot', 25)

surf = Ability('surf', 15)
hydro_cannon = Ability('hydro_cannon', 35)
water_gun = Ability('water_gun', 20)

overheat = Ability('overheat', 10)
blast_burn = Ability('blast_burn', 45)
flamethrower = Ability('flamethrower', 15)

bulbasaur.learn(razor_leaf)
bulbasaur.learn(frenzy_plant)

squirtle.learn(surf)
squirtle.learn(hydro_cannon)

charmander.learn(flamethrower)
charmander.learn(blast_burn)

chikorita.learn(grass_knot)
chikorita.learn(frenzy_plant)

totodile.learn(water_gun)
totodile.learn(surf)

cyndaquil.learn(blast_burn)
cyndaquil.learn(overheat)



pokedex = [bulbasaur, squirtle, charmander, chikorita, totodile, cyndaquil]
