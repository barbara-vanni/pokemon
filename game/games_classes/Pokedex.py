import json
import random
from game.games_classes.Pokemon import *

class Pokedex:
    def __init__(self):
        self.pokemon_list = []
    
    def load_from_json(self, json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            for pokemon_data in data["pokemon_list"]:
                # print(f"Debug: Loading Pokemon - {pokemon_data['name']} - Statut: {pokemon_data['statut']}")  # Debug line
                image_front = pokemon_data.get("image_front", "chemin/par/defaut/image.png")
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
                    image_front,
                    pokemon_data["statut"],
                    pokemon_data["in_stockage"]
                )
                self.pokemon_list.append(pokemon)
                pokemon.set_statut(pokemon_data["statut"])

    def print_pokemon_meet(self):
        for pokemon in self.pokemon_list:
            if pokemon.get_statut() == 1:
                print(f"Name: {pokemon.get_name()}")
                # print(f"Type: {pokemon.get_types()}")
                # print(f"Level: {pokemon.get_level()}")
                # print(f"Attack: {pokemon.get_power_attack()}")
                # print(f"Defense: {pokemon.get_defense()}")
                # print(f"Speed: {pokemon.get_speed()}")
                # print(f"Pv: {pokemon.get_pv()}/{pokemon.get_pv_max()}")
                # print(f"Xp: {pokemon.get_xp()}/{pokemon.get_xp_max()}\n")



    def choose_random_pokemon(self):
        available_pokemon = [pokemon for pokemon in self.pokemon_list if pokemon.get_statut() == 0]

        chosen_pokemon = random.choice(available_pokemon)
        return chosen_pokemon

    def change_statut(self, pokemon_name):
        json_file_path = "game/games_classes/pokedex.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name:
                pokemon_data["statut"] = 1
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)


# pokedex = Pokedex()
# pokedex.load_from_json("game/games_classes/pokedex.json")

# random_pokemon = pokedex.choose_random_pokemon()

# if random_pokemon:
#     print("Randomly Chosen Pokemon:")
#     random_pokemon.informations_pokemon()

