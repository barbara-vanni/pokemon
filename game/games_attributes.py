from .games_classes.Pokemon import *
from .games_classes.Pokedex import *
from .games_classes.Combat import *

pokemon_types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

pokemon_matrice = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
    [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 1, 0.5, 1],
    [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
    [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 0.5, 1],
    [1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 0.5, 2, 1, 0.5, 2, 1, 0.5, 1],
    [1, 2, 1, 1, 2, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 2, 1, 0.5, 1],
    [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],
    [1, 1, 1, 1, 0.5, 1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 0.5, 2],
    [1, 2, 1, 2, 0.5, 2, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 0.5],
    [1, 1, 1, 0.5, 2, 1, 2, 1, 0, 1, 1, 2, 0.5, 1, 1, 0.5, 1, 1],
    [1, 1, 1, 1, 1, 1, 0.5, 2, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 0, 1],
    [1, 0.5, 2, 1, 2, 1, 0.5, 0.5, 1, 2, 1, 1, 1, 0.5, 1, 0.5, 1, 1],
    [1, 2, 1, 0, 1, 2, 0.5, 2, 0.5, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0.5, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0.5, 1, 0.5, 1, 2],
    [0.5, 2, 1, 1, 0.5, 0.5, 2, 0, 2, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 2],
    [1, 1, 1, 1, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 1, 1, 0, 0.5, 2, 1]   
]

pokemon1 = Pokemon("Carapuce", pokemon_types[2], 1, 20, 10, 10, 100, 100, 0, 100, "assets/images/pokemon_front/carapuce.png", pokemon_matrice)
pokedex = Pokedex()
pokedex.load_from_json("game/games_classes/pokedex.json")
pokemon2 = pokedex.choose_random_pokemon()
pokedex.change_statut(pokemon2.get_name())
pokedex.print_pokemon_meet()
combat_begin = Combat(pokemon1, pokemon2, 0, 0, [], [], 0)
# trainer = Trainer([pokemon4, pokemon2, pokemon7], pokemon4)
