import json
from Pokemon import *

class Pokedex(Pokemon):
    def __init__(self, name, types, matrice, power_attack, defense, speed, pv, pv_max, xp, level, xp_max = 200, statut = False):
        Pokemon.__init__(self, name, types, matrice, power_attack, defense, speed, pv, pv_max, xp, level, xp_max = 200, statut = False)
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
                print(f"Name: {pokemon.get_name()}")
                print(f"Type: {pokemon.get_types()}")
                print(f"Level: {pokemon.get_level()}")
                print(f"Attack: {pokemon.get_power_attack()}")
                print(f"Defense: {pokemon.get_defense()}")
                print(f"Speed: {pokemon.get_speed()}")
                print(f"Pv: {pokemon.get_pv()}/{pokemon.get_pv_max()}")
                print(f"Xp: {pokemon.get_xp()}/{pokemon.get_xp_max()}\n")

pokedex = Pokedex("name", "types", "matrice", "power_attack", "defense", "speed", "pv", "pv_max", "xp", "level", "xp_max", "statut")

pokedex.load_from_json("game/games_classes/pokedex.json")

pokedex.print_pokemon_meet()
