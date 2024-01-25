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

    def choose_random_pokemon(self):
        available_pokemon = [pokemon for pokemon in self.pokemon_list if pokemon.get_statut() == 0]
        chosen_pokemon = random.choice(available_pokemon)
        chosen_pokemon.set_image_front(f"assets/images/pokemon_front/{chosen_pokemon.get_name().lower()}.png")
        return chosen_pokemon

    def choose_specific_pokemon(self, pokemon_name):
        for pokemon in self.pokemon_list:
            if pokemon.get_name() == pokemon_name:
                return pokemon
        return None

    def choose_your_name(self, name_trainer):
        # self.__name_trainer = input("Choisissez votre nom de dresseur: ")
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open("game/games_classes/pokedex.json", "r") as pokedex_file:
            pokedex_data = json.load(pokedex_file)
        with open(json_file_path, "w") as new_file:
            json.dump(pokedex_data, new_file, indent=2)    

    def change_statut(self, pokemon_name, name_trainer):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name:
                pokemon_data["statut"] = 1
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)

    def get_pokemon_by_type(self, pokemon_type):
        matching_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon_type in pokemon.get_types():
                matching_pokemon.append(pokemon)
        return matching_pokemon
    
    def get_pokemon_by_name(self, pokemon_name):
        matching_pokemon = []
        for pokemon in self.pokemon_list:
            if pokemon_name in pokemon.get_name():
                matching_pokemon.append(pokemon)
        return matching_pokemon

    def change_statistics(self, pokemon_name, xp, xp_max, name_trainer):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name:
                pokemon_data["level"] += 1
                pokemon_data["power_attack"] += 1
                pokemon_data["defense"] += 1
                pokemon_data["speed"] += 1
                pokemon_data["pv_max"] += 1
                pokemon_data["pv"] += 1
                pokemon_data["xp_max"] = xp_max
                pokemon_data["xp"] = xp 
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)


    def change_stat_xp(self, pokemon_name, name_trainer):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name:
                pokemon_data["xp"] += 100
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)

    def change_stat_pv(self, pokemon_name, pv, name_trainer):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name:
                pokemon_data["pv"] = pv
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)