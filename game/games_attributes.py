from .games_classes import *

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

pokemon1 = Pokemon("Tortank", pokemon_types[2], pokemon_matrice, 20, 10, 12, 100, 100, 0, 1)
pokemon2 = Pokemon("Salameche", pokemon_types[1], pokemon_matrice, 20, 10, 10, 100, 100, 0, 1)
combat_begin = Combat(pokemon1, pokemon2, 0, 0, [], [], 0, '')

