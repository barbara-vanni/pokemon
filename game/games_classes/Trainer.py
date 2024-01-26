from .Pokemon import *
from .Pokedex import *
import json

class Trainer():
    def __init__(self, pokemon_list, actif_pokemon, name_trainer, enemy_list):
        self.__pokemon_list = pokemon_list
        self.__actif_pokemon = actif_pokemon
        self.__name_trainer = name_trainer
        self.__enemy_list = enemy_list

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

    def get_enemy_list(self):
        return self.__enemy_list
    def set_enemy_list(self, enemy_list):
        self.__enemy_list = enemy_list

    def add_pokemon(self, new_pokemon):
        if new_pokemon not in self.__pokemon_list and len(self.__pokemon_list) < 6:
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

    def enemy_pocket(self, pokedex):
        while len(self.__enemy_list) < 6:
            choose_random_pokemon = pokedex.choose_random_pokemon()
            if choose_random_pokemon not in self.__enemy_list:
                self.__enemy_list.append(choose_random_pokemon)
        return self.__enemy_list


    def show_enemy_list(self):
        for pokemon in self.__enemy_list:
            print(pokemon.get_name())


# trainer = Trainer([], None, "Sacha", [])
# pokemon1 = Pokemon("Pikachu", 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, "Electric")
# pokemon2 = Pokemon("Carapuce", 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, "Water")
# pokemon3 = Pokemon("Bulbizarre", 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, "Grass")
# pokemon4 = Pokemon("Salameche", 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, "Fire")
# pokemon5 = Pokemon("Rattata", 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, "Normal")
# pokemon6 = Pokemon("Piafabec", 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, "Normal")

# trainer.add_pokemon(pokemon1)
# trainer.add_pokemon(pokemon2)
# trainer.add_pokemon(pokemon3)
# trainer.add_pokemon(pokemon4)
# trainer.add_pokemon(pokemon5)
# trainer.add_pokemon(pokemon6)
# trainer.show_pokemon_list()

# trainer.enemy_pocket()


