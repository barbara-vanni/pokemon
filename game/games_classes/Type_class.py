class Type:
    # Constructeur
    def __init__(self, types, matrice):
        self._types = types
        self._matrice = matrice


    # Types
    def get_types(self):
        return self._types

    def set_types(self, types):
        self._types = types

    # Matrice
    def get_matrice(self):
        return self._matrice

    def set_matrice(self, matrice):
        self._matrice = matrice

types_pokemon = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "Ggost", "dragon", "dark", "steel", "fairy"]

matrice_pokemon = [
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

type_pokemon = Type(types_pokemon, matrice_pokemon)

# type1 = "water"
# type2 = "fire"
# print(type_pokemon.get_matrice()[type_pokemon.get_types().index(type1)][type_pokemon.get_types().index(type2)])

