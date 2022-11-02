from pokemon import PokemonType
from ability import Ability, AbilityType

razor_leaf = Ability('razor_leaf', 55, 95, AbilityType.GRASS)
frenzy_plant = Ability('frenzy_plant', 150, 90, AbilityType.GRASS)
grass_knot = Ability('grass_knot', 80, 100, AbilityType.GRASS)

surf = Ability('surf', 90, 100, AbilityType.WATER)
hydro_cannon = Ability('hydro_cannon', 150, 90, AbilityType.WATER)
water_gun = Ability('water_gun', 40, 100, AbilityType.WATER)

overheat = Ability('overheat', 130, 90, AbilityType.FIRE)
blast_burn = Ability('blast_burn', 150, 90, AbilityType.FIRE)
flamethrower = Ability('flamethrower', 90, 100, AbilityType.FIRE)

bulbasaur = {'name': 'bulbasaur', 'damage': 49, 'max_hp': 450, 'speed': 45,
             'type': [PokemonType.GRASS, PokemonType.POISON], 'abilities': [razor_leaf, frenzy_plant]}
squirtle = {'name': 'squirtle', 'damage': 48, 'max_hp': 440, 'speed': 43,
            'type': [PokemonType.WATER], 'abilities': [surf, hydro_cannon]}
charmander = {'name': 'charmander', 'damage': 52, 'max_hp': 390, 'speed': 65,
              'type': [PokemonType.FIRE], 'abilities': [flamethrower, blast_burn]}

chikorita = {'name': 'chikorita', 'damage': 49, 'max_hp': 450, 'speed': 45,
             'type': [PokemonType.GRASS], 'abilities': [grass_knot, frenzy_plant]}
totodile = {'name': 'totodile', 'damage': 65, 'max_hp': 500, 'speed': 43,
            'type': [PokemonType.WATER], 'abilities': [water_gun, surf]}
cyndaquil = {'name': 'cyndaquil', 'damage': 52, 'max_hp': 390, 'speed': 65,
             'type': [PokemonType.FIRE], 'abilities': [blast_burn, overheat]}

lapras = {'name': 'lapras', 'damage': 80, 'max_hp': 600, 'speed': 80,
          'type': [PokemonType.WATER, PokemonType.ICE], 'abilities': [hydro_cannon, surf]}
arcanine = {'name': 'arcanine', 'damage': 90, 'max_hp': 500, 'speed': 70,
            'type': [PokemonType.FIRE], 'abilities': [blast_burn, overheat]}
koffing = {'name': 'koffing', 'damage': 40, 'max_hp': 400, 'speed': 50,
           'type': [PokemonType.POISON], 'abilities': [frenzy_plant, hydro_cannon]}

mewtwo = {'name': 'mewtwo', 'damage': 250, 'max_hp': 500, 'speed': 120,
          'type': [PokemonType.POISON], 'abilities': [hydro_cannon, blast_burn]}


grass = [bulbasaur, squirtle, charmander, chikorita, totodile, cyndaquil]

land = [lapras, arcanine, koffing]

cave = [mewtwo]