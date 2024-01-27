import json
import random
from game.games_classes.Pokemon import *
from game.games_classes.Trainer import *


class Pokedex:
    def __init__(self):
        self.pokemon_list = []
        self.pokemon_trainer = []

    def load_from_json(self, json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            for pokemon_data in data["pokemon_list"]:
                #print(f"Debug: Loading Pokemon - {pokemon_data['name']} - Statut: {pokemon_data['statut']}")  # Debug line
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
                    pokemon_data["evolution_level"],
                    pokemon_data["evolution_name"],
                    pokemon_data["statut"],
                    pokemon_data["in_stockage"]
                )
                self.pokemon_list.append(pokemon)
                pokemon.set_statut(pokemon_data["statut"])
                self.pokemon_trainer.append(pokemon)
                
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
        json_file_path = f'game/games_classes/{name_trainer}.json'
        with open("game/games_classes/pokedex.json", "r") as pokedex_file:
            pokedex_data = json.load(pokedex_file)
        with open(json_file_path, "w") as newfile:
            json.dump(pokedex_data, newfile, indent=2)

       
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

    def change_statistics(self, pokemon_name, xp, name_trainer):
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
                pokemon_data["xp_max"] = 150 + 100 * pokemon_data["level"] 
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

    def get_level_scale(self, pokemon_name):
        if pokemon_name.get_level() == 1:
            return 0
        elif pokemon_name.get_level() >= 40:
            return 3
        elif pokemon_name.get_level() >= 15:
            return 2
        else:
            return 1
    
    def stats_level_scale(self, pokemon_name):
        pokemon_name.set_power_attack(pokemon_name.get_power_attack() + pokemon_name.get_level())
        pokemon_name.set_defense(pokemon_name.get_defense() + pokemon_name.get_level())
        pokemon_name.set_speed(pokemon_name.get_speed() + pokemon_name.get_level())
        pokemon_name.set_pv(pokemon_name.get_pv() + pokemon_name.get_level())
        pokemon_name.set_pv_max(pokemon_name.get_pv_max() + pokemon_name.get_level())

    def change_statistics_down(self, pokemon_name, name_trainer):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name.get_name():
                if pokemon_data ["level"] >= 2:
                    scale = self.get_level_scale(pokemon_name)
                    pokemon_data["level"] -= scale
                    pokemon_data["power_attack"] -= scale
                    pokemon_data["defense"] -= scale
                    pokemon_data["speed"] -= scale
                    pokemon_data["pv_max"] -= scale
                    pokemon_data["pv"] = pokemon_name.get_pv_max() - scale
                    pokemon_data["xp_max"] = 150 + 100 * pokemon_data["level"] 
                    pokemon_data["xp"] = 0
                with open(json_file_path, "w") as file:
                    json.dump(data, file, indent=2)
    
    def evolution(self, pokemon_name, name_trainer):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)
        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name.get_name():
                if pokemon_data["level"] == pokemon_name.get_evolution_level():
                    return True
    
    # def change_pokemon_trainer(self, pokemon_name, name_trainer):
    #     json_file_path = f"game/games_classes/{name_trainer}.json"
    #     with open(json_file_path, "r") as file:
    #         data = json.load(file)
    #     for pokemon_data in data["pokemon_list"]:
    #         if pokemon_data["name"] == pokemon_name.get_name():
    #             pokemon_data["name"] = pokemon_name.get_evolution_name()
    #             pokemon_data["level"] = pokemon_name.get_evolution_level()
    #             pokemon_data["power_attack"] = pokemon_name.get_power_attack()
    #             pokemon_data["defense"] = pokemon_name.get_defense()
    #             pokemon_data["speed"] = pokemon_name.get_speed()
    #             pokemon_data["pv_max"] = pokemon_name.get_pv_max()
    #             pokemon_data["pv"] = pokemon_name.get_pv()
    #             pokemon_data["xp_max"] = pokemon_name.get_xp_max()
    #             pokemon_data["xp"] = pokemon_name.get_xp()
    #             pokemon_data["evolution_level"] = pokemon_name.get_evolution_level()
    #             pokemon_data["evolution_name"] = pokemon_name.get_evolution_name()
    #             pokemon_data["statut"] = pokemon_name.get_statut()
    #             pokemon_data["in_stockage"] = pokemon_name.get_in_stockage()
    #     with open(json_file_path, "w") as file:
    #         json.dump(data, file, indent=2)

    # def change_pokemon_trainer(self, name_trainer, pokemon_name):
    #     json_file_path = f"game/games_classes/{name_trainer}.json"
    #     with open(json_file_path, "r") as file:
    #         data = json.load(file)

    #     for pokemon_data in data["pokemon_list"]:
    #         if pokemon_data["name"] == pokemon_name.get_name():
    #             # Copier les statistiques dans un nouvel objet Pokemon
    #             specific_pokemon = Pokemon(
    #                 pokemon_data["name"] == pokemon_name.get_name(),
    #                 pokemon_data["types"] == pokemon_name.get_types(),
    #                 pokemon_data["level"] == pokemon_name.get_level(),
    #                 pokemon_data["power_attack"] == pokemon_name.get_power_attack(),
    #                 pokemon_data["defense"] == pokemon_name.get_defense(),
    #                 pokemon_data["speed"] == pokemon_name.get_speed(),
    #                 pokemon_data["pv"] == pokemon_name.get_pv(),
    #                 pokemon_data["pv_max"] == pokemon_name.get_pv_max(),
    #                 pokemon_data["xp"] == pokemon_name.get_xp(),
    #                 pokemon_data["xp_max"] == pokemon_name.get_xp_max(),
    #                 pokemon_data.get("image_front") == pokemon_name.get_image_front(),
    #                 pokemon_data["evolution_level"] == pokemon_name.get_evolution_level(),
    #                 pokemon_data["evolution_name"]  == pokemon_name.get_evolution_name(),
    #                 pokemon_data["statut"] == pokemon_name.get_statut(),
    #                 pokemon_data["in_stockage"] == pokemon_name.get_in_stockage()
    #             )

    #             # Ajouter le nouvel objet à la liste pokemon_trainer
    #             self.pokemon_trainer.append(specific_pokemon)

    #     with open(json_file_path, "w") as file:
    #         json.dump(data, file, indent=2)

    def change_pokemon_trainer(self, name_trainer, pokemon_name):
        json_file_path = f"game/games_classes/{name_trainer}.json"
        with open(json_file_path, "r") as file:
            data = json.load(file)

        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name.get_name():
                # Ajouter le Pokémon existant à la liste pokemon_trainer
                self.pokemon_trainer.append(pokemon_data)
                # Retirer le Pokémon de la liste pokemon_list
                data["pokemon_list"].remove(pokemon_data)

        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)



    def reset_stats(self, pokemon_name, name_trainer):
        json_file_path_trainer = f"game/games_classes/{name_trainer}.json"
        json_file_path_pokedex = "game/games_classes/pokedex.json"

        # Charger le fichier du dresseur
        with open(json_file_path_trainer, "r") as trainer_file:
            try:
                trainer_data = json.load(trainer_file)
            except json.JSONDecodeError:
                # Gérer l'erreur si le fichier du dresseur est vide ou mal formaté
                print("Erreur de chargement du fichier du dresseur.")
                return

        # Charger le fichier pokedex.json
        with open(json_file_path_pokedex, "r") as pokedex_file:
            try:
                pokedex_data = json.load(pokedex_file)
            except json.JSONDecodeError:
                # Gérer l'erreur si le fichier pokedex.json est vide ou mal formaté
                print("Erreur de chargement du fichier pokedex.")
                return

        # Rechercher le Pokémon dans la liste du dresseur
        if pokemon_name.get_name() in trainer_data:
            # Trouver l'entrée correspondante dans le pokedex
            for pokedex_entry in pokedex_data["pokemon_list"]:
                if pokedex_entry["name"] == pokemon_name.get_name():
                    # Mettre à jour les statistiques du Pokémon dans le fichier du dresseur
                    trainer_data[pokemon_name.get_name()] = pokedex_entry

            # Enregistrer les données mises à jour dans le fichier du dresseur
            with open(json_file_path_trainer, "w") as trainer_file:
                json.dump(trainer_data, trainer_file, indent=2)
                print(f"Statistiques de {pokemon_name.get_name()} réinitialisées avec succès.")
        else:
            print(f"{pokemon_name.get_name()} n'a pas été trouvé dans le fichier du dresseur.")

    def adjust_level(self, pokemon_name, name_trainer, level_stockage):
        json_file_path = f"game/games_classes/{name_trainer}.json"

        with open(json_file_path, "r") as file:
            data = json.load(file)

        for pokemon_data in data["pokemon_list"]:
            if pokemon_data["name"] == pokemon_name.get_name():
                pokemon_data["level"] = level_stockage
                pokemon_data["power_attack"] += level_stockage
                pokemon_data["defense"] += level_stockage
                pokemon_data["speed"] += level_stockage
                pokemon_data["pv_max"] += level_stockage
                pokemon_data["pv"] = pokemon_name.get_pv_max() + level_stockage
                pokemon_data["xp_max"] = 150 + 100 * pokemon_data["level"]
                pokemon_data["xp"] = 0

        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=2)

    