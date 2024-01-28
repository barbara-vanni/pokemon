from .Pokemon import *
from .Pokedex import *
import json

class Trainer():
    def __init__(self, pokemon_list, actif_pokemon, name_trainer, catch_chance_ratio):
        self.__pokemon_list = pokemon_list
        self.__actif_pokemon = actif_pokemon
        self.__name_trainer = name_trainer
        self.__catch_chance_ratio = catch_chance_ratio
    

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

    def get_catch_chance_ratio(self):
        return self.__catch_chance_ratio
    def set_catch_chance_ratio(self, catch_chance_ratio):
        self.__catch_chance_ratio = catch_chance_ratio

    def add_pokemon(self, new_pokemon):
        if new_pokemon not in self.__pokemon_list and len(self.__pokemon_list) < 6:
            self.__pokemon_list.append(new_pokemon)
            if len(self.__pokemon_list) == 1:
                self.__actif_pokemon = new_pokemon
                
    
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



    def potion(self):
        self.__actif_pokemon.set_pv(self.__actif_pokemon.get_pv() + 20)
        if self.__actif_pokemon.get_pv() >= self.__actif_pokemon.get_pv_max():
            self.__actif_pokemon.set_pv(self.__actif_pokemon.get_pv_max())

    def pokeball(self):
        catch_chance = random.randint(0, 100)
        if catch_chance <= 33 :
            return self.__catch_chance_ratio == 0
        else:
            return self.__catch_chance_ratio == 1





