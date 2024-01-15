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

pokemon1 = Pokemon("Tortank", pokemon_types[2], pokemon_matrice, 20, 10, 10, 100, 100, 0, 1)
pokemon2 = Pokemon("Pikachu", pokemon_types[1], pokemon_matrice, 15, 8, 12, 80, 80, 0, 1)
pokemon3 = Pokemon("Dracaufeu", pokemon_types[3], pokemon_matrice, 25, 12, 8, 120, 120, 0, 1)
pokemon4 = Pokemon("Bulbizarre", pokemon_types[0], pokemon_matrice, 18, 9, 11, 90, 90, 0, 1)
pokemon5 = Pokemon("Mewtwo", pokemon_types[4], pokemon_matrice, 30, 15, 15, 150, 150, 0, 1)
pokemon6 = Pokemon("Jigglypuff", pokemon_types[1], pokemon_matrice, 12, 6, 18, 60, 60, 0, 1)
pokemon7 = Pokemon("Gyarados", pokemon_types[3], pokemon_matrice, 28, 14, 7, 140, 140, 0, 1)
pokemon8 = Pokemon("Alakazam", pokemon_types[4], pokemon_matrice, 22, 11, 9, 110, 110, 0, 1)
pokemon9 = Pokemon("Venusaur", pokemon_types[0], pokemon_matrice, 24, 12, 11, 120, 120, 0, 1)
pokemon10 = Pokemon("Charizard", pokemon_types[3], pokemon_matrice, 26, 13, 10, 130, 130, 0, 1)
combat_begin = Combat(pokemon1, pokemon2, 0, 0, [], [], 0)
trainer = Trainer([pokemon4, pokemon2, pokemon7], pokemon4)