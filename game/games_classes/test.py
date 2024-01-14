import json

class Pokemon:
    def __init__(self, name, types, power_attack, defense, speed, pv, pv_max, xp, level, xp_max=200, statut=False):
        self._name = name
        self._types = types
        self._power_attack = power_attack
        self._defense = defense
        self._speed = speed
        self._pv = pv
        self._pv_max = pv_max
        self._xp = xp
        self._xp_max = xp_max
        self._level = level
        self._statut = statut
    # name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Types
    def get_types(self):
        return self._types

    def set_types(self, types):
        self._types = types

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

    def set_speed(self, speed):
        self._speed = speed

    # Pv
    def get_pv(self):
        return self._pv

    def set_pv(self, pv):
        self._pv = max(pv, 0)

    # Pv_max
    def get_pv_max(self):
        return self._pv_max

    def set_pv_max(self, pv_max):
        self._pv_max = pv_max

    # Xp
    def get_xp(self):
        return self._xp

    def set_xp(self, xp):
        self._xp = xp

    # Xp_max
    def get_xp_max(self):
        return self._xp_max

    def set_xp_max(self, xp_max):
        self._xp_max = xp_max

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




class Pokedex:
    def __init__(self):
        self.pokemon_list = []

    def load_from_json(self, json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            for pokemon_data in data["pokemon_list"]:
                pokemon = Pokemon(
                    pokemon_data["name"],
                    pokemon_data["types"],
                    pokemon_data["power_attack"],
                    pokemon_data["defense"],
                    pokemon_data["speed"],
                    pokemon_data["pv"],
                    pokemon_data["pv_max"],
                    pokemon_data["xp"],
                    pokemon_data["level"],
                    pokemon_data["xp_max"],
                    pokemon_data["statut"]
                )
                self.pokemon_list.append(pokemon)

    def print_pokemon_meet(self):
        for pokemon in self.pokemon_list:
            if pokemon.get_statut():
                print(f"Name : {pokemon.get_name()}")
                print(f"Type : {pokemon.get_types()}")
                print(f"Level : {pokemon.get_level()}")
                print(f"Attack : {pokemon.get_power_attack()}")
                print(f"Defense : {pokemon.get_defense()}")
                print(f"Speed : {pokemon.get_speed()}")
                print(f"Pv : {pokemon.get_pv()}/{pokemon.get_pv_max()}")
                print(f"Xp : {pokemon.get_xp()}/{pokemon.get_xp_max()}\n")


pokedex = Pokedex()

pokedex.load_from_json("game/games_classes/pokedex.json")

pokedex.print_pokemon_meet()
