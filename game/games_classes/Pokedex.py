import json
from Pokemon import Pokemon
from Type import *
import random

class Pokedex:
    def __init__(self):
        self.pokemon_list = []
    
    def load_from_json(self, json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            for pokemon_data in data["pokemon_list"]:
                print(f"Debug: Loading Pokemon - {pokemon_data['name']} - Statut: {pokemon_data['statut']}")  # Debug line
                pokemon = Pokemon(
                    pokemon_data["name"],
                    pokemon_data["types"],
                    pokemon_data["level"],
                    pokemon_data["power_attack"],
                    pokemon_data["defense"],
                    pokemon_data["speed"],
                    pokemon_data["pv"],
                    pokemon_data["pv_max"],
                    pokemon_data["xp"],
                    pokemon_data["xp_max"],
                    pokemon_data["statut"]
                )
                self.pokemon_list.append(pokemon)
                pokemon.set_statut(pokemon_data["statut"])

    def print_pokemon_meet(self):
        for pokemon in self.pokemon_list:
            if pokemon.get_statut() == 1:
                print(f"Name: {pokemon.get_name()}")
                print(f"Type: {pokemon.get_types()}")
                print(f"Level: {pokemon.get_level()}")
                print(f"Attack: {pokemon.get_power_attack()}")
                print(f"Defense: {pokemon.get_defense()}")
                print(f"Speed: {pokemon.get_speed()}")
                print(f"Pv: {pokemon.get_pv()}/{pokemon.get_pv_max()}")
                print(f"Xp: {pokemon.get_xp()}/{pokemon.get_xp_max()}\n")
    def choose_random_pokemon(self):
        available_pokemon = [pokemon for pokemon in self.pokemon_list if pokemon.get_statut() == 0]

        chosen_pokemon = random.choice(available_pokemon)
        return chosen_pokemon


pokedex = Pokedex()
pokedex.load_from_json("game/games_classes/pokedex.json")
pokedex.print_pokemon_meet()

random_pokemon = pokedex.choose_random_pokemon()

if random_pokemon:
    print("Randomly Chosen Pokemon:")
    random_pokemon.informations_pokemon()