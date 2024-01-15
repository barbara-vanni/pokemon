from .Pokemon import *

class Trainer():
    def __init__(self, pokemon_list, actif_pokemon, new_pokemon):
        self.__pokemon_list = pokemon_list
        self.__actif_pokemon = actif_pokemon
        self.__new_pokemon = new_pokemon

    def get_pokemon_list(self):
        return self.__pokemon_list
    def set_pokemon_list(self, pokemon_list):
        self.__pokemon_list = pokemon_list

    def get_actif_pokemon(self):
        return self.__actif_pokemon
    def set_actif_pokemon(self, actif_pokemon):
        self.__actif_pokemon = actif_pokemon

    def get_new_pokemon(self):
        return self.__new_pokemon
    def set_new_pokemon(self, new_pokemon):
        self.__new_pokemon = new_pokemon

    def add_pokemon(self):
        if self.__new_pokemon not in self.__pokemon_list and len(self.__pokemon_list) < 5:
            self.__pokemon_list.append(self.__new_pokemon)
    
    def remove_pokemon(self):
        self.__pokemon_list.remove(self.__actif_pokemon)

    def change_pokemon(self):
        if self.__new_pokemon in self.__pokemon_list:
            self.__actif_pokemon = self.__new_pokemon
    
    def show_pokemon_list(self):
        for i in self.__pokemon_list:
            print(self.__pokemon_list[i])

# Supposons que vous ayez déjà importé la classe Pokemon et défini pokemon_types et pokemon_matrice

pokemon1 = Pokemon("Tortank", pokemon_types[2], pokemon_matrice, 20, 10, 10, 100, 100, 0, 1)
pokemon2 = Pokemon("Pikachu", pokemon_types[1], pokemon_matrice, 15, 8, 12, 80, 80, 0, 1)
pokemon3 = Pokemon("Dracaufeu", pokemon_types[3], pokemon_matrice, 25, 12, 8, 120, 120, 0, 1)
pokemon4 = Pokemon("Bulbizarre", pokemon_types[0], pokemon_matrice, 18, 9, 11, 90, 90, 0, 1)
pokemon5 = Pokemon("Mewtwo", pokemon_types[4], pokemon_matrice, 30, 15, 15, 150, 150, 0, 1)
pokemon6 = Pokemon("Jigglypuff", pokemon_types[1], pokemon_matrice, 12, 6, 18, 60, 60, 0, 1)
pokemon7 = Pokemon("Gyarados", pokemon_types[3], pokemon_matrice, 28, 14, 7, 140, 140, 0, 1)
pokemon8 = Pokemon("Alakazam", pokemon_types[4], pokemon_matrice, 22, 11, 9, 110, 110, 0, 1)
pokemon9 = Pokemon("Venusaur", pokemon_types[0], pokemon_matrice, 24, 12, 11, 120, 120, 0, 1)
pokemon10 = Pokemon("Charizard", pokemon_types[3], pokemon_matrice, 26, 13, 10, 130, 130, 0, 1)

trainer = Trainer([pokemon4, pokemon2, pokemon7], pokemon4, pokemon5)
trainer.show_pokemon_list()