from Type import *


class Pokemon(Type):
    # Constructeur
    def __init__(self, types, matrice, power_attack, defense, speed, pv, xp, level, statut = False):
        Type.__init__(self, types, matrice)
        self._power_attack = power_attack
        self._defense = defense
        self._speed = speed
        self._pv = pv
        self._xp = xp
        self._level = level
        self._statut = statut

    # Power_attack
    def get_power_attack(self):
        return self._power_attack

    def set_power_attack(self, power_attack):
        self._power_attack = power_attack

    # Defense
    def get_defense(self):
        return self._defense

    def set_defense(self, defense):
        self._defense = defense

    # Speed
    def get_speed(self):
        return self._speed

    def set_speed(slef, speed):
        self._speed = speed

    # Pv
    def get_pv(self):
        return self._pv

    def set_pv(self, pv):
        self._pv = pv

    # Xp
    def get_xp(self):
        return self._xp

    def set_xp(self, xp):
        self._xp = xp

    # Level
    def get_level(self):
        return self._level

    def set_level(self, level):
        self._level = level

    # Statut
    def get_statut(self):
        return self._statut

    def set_statut(self, statut):
        self._statut = statut

   
    # other methods
    def informations_pokemon(self):
        print(f"Type : {self._types}")
        print(f"Attack : {self._power_attack}")
        print(f"Defense : {self._defense}")
        print(f"Speed : {self._speed}")
        print(f"Pv : {self._pv}")
        print(f"Xp : {self._xp}")
        print(f"Level : {self._level}\n")


pokemon1 = Pokemon(pokemon_types[2], pokemon_matrice, 10, 10, 10, 10, 10, 10)
pokemon1.informations_pokemon()

pokemon2 = Pokemon(pokemon_types[1], pokemon_matrice, 10, 10, 10, 10, 10, 10) 
pokemon2.informations_pokemon()

type1 = pokemon1.get_types()
type2 = pokemon2.get_types()

index1 = type_pokemon.get_types().index(type1)
index2 = type_pokemon.get_types().index(type2)

weakness_resistance = type_pokemon.get_matrice()[index1][index2]

print(f"Affinity between {type1} and {type2} : {weakness_resistance}")