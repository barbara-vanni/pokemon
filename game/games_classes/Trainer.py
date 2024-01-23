from .Pokemon import *
import json

class Trainer():
    def __init__(self, pokemon_list, actif_pokemon, name_trainer):
        self.__pokemon_list = pokemon_list
        self.__actif_pokemon = actif_pokemon
        self.__name_trainer = name_trainer

    def get_pokemon_list(self):
        return self.__pokemon_list
    def set_pokemon_list(self, pokemon_list):
        self.__pokemon_list = pokemon_list

    def get_actif_pokemon(self):
        return self.__actif_pokemon
    def set_actif_pokemon(self, actif_pokemon):
        self.__actif_pokemon = actif_pokemon

    def get_name_trainer(self):
        return self.__name_trainer
    def set_name_trainer(self, name_trainer):
        self.__name_trainer = name_trainer

    def add_pokemon(self, new_pokemon):
        if new_pokemon not in self.__pokemon_list and len(self.__pokemon_list) < 5:
            self.__pokemon_list.append(new_pokemon)
    
    def remove_pokemon(self, pokemon_to_remove):
        if pokemon_to_remove in self.__pokemon_list:
            self.__pokemon_list.remove(pokemon_to_remove)
        else:
            print("Ce pokemon n'est pas dans votre inventaire")

    def change_pokemon(self, new_pokemon_actif):
        if new_pokemon_actif in self.__pokemon_list:
            self.__actif_pokemon = new_pokemon_actif
        else:
            print("Ce pokemon n'est pas dans votre inventaire")
    
    def show_pokemon_list(self):
        for pokemon in self.__pokemon_list:
            print(pokemon.get_name())


    def show_pokemon_actif(self):
        print(self.__actif_pokemon.get_name())

    # def choose_your_name(self):
    #     self.__name_trainer = input("Choisissez votre nom de dresseur: ")
    #     json_file_path = "game/games_classes/{self.__name_trainer}.json"
    #     with open(json_file_path, "w") as file:
    #         data = json.load(file)
    #         json.dump(data, file, indent=2)4
    
    def choose_your_name(self):
        self.__name_trainer = input("Choisissez votre nom de dresseur: ")
        json_file_path = f"game/games_classes/{self.__name_trainer}.json"
        with open("game/games_classes/pokedex.json", "r") as pokedex_file:
            pokedex_data = json.load(pokedex_file)
        with open(json_file_path, "w") as new_file:
            json.dump(pokedex_data, new_file, indent=2)
