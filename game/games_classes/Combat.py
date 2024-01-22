# import random
# from .Pokemon import *
# from graphics.graphics_attributes import *

# class Combat:
#     def __init__(self, pokemon1, pokemon2, attack_chance_ratio, affinity_values, player_list, computer_list, states, render_message):
#         self.__pokemon_player = pokemon1.get_name()
#         self.__pokemon_computer = pokemon2
#         self.__pokemon1 = pokemon1
#         self.__pokemon2 = pokemon2
#         self.__attack_chance_ratio = attack_chance_ratio
#         self.__affinity_values = affinity_values
#         self.__player_list = player_list
#         self.__computer_list = computer_list
#         self.__states = states
#         self.__render_message = render_message

#     def get_pokemon_player(self):
#         return self.__pokemon_player
#     def set_pokemon_player(self, pokemon1):
#         self.__pokemon_player = pokemon1

#     def get_pokemon1(self):
#         return self.__pokemon1
#     def set_pokemon1(self, pokemon1):
#         self.__pokemon1 = pokemon1

#     def get_pokemon2(self):
#         return self.__pokemon2
#     def set_pokemon2(self, pokemon2):
#         self.__pokemon2 = pokemon2

#     def get_attack_chance_ratio(self):
#         return self.__attack_chance_ratio
#     def set_attack_chance_ratio(self, attack_chance_ratio):
#         self.__attack_chance_ratio = attack_chance_ratio
    
#     def get_affinity_values(self):
#         return self.__affinity_values
#     def set_affinity_values(self, affinity_values):
#         self.__affinity_values = affinity_values
    
#     def get_player_list(self):
#         return self.__player_list
#     def set_player_list(self, player_list):
#         self.__player_list = player_list

#     def get_computer_list(self):
#         return self.__computer_list
#     def set_computer_list(self, computer_list):
#         self.__computer_list = computer_list

#     def get_states(self):
#         return self.__states
#     def set_states(self, states):
#         self.__states = states

#     def get_render_message(self):
#         return self.__render_message
#     def set_render_message(self, render_message):
#         self.__render_message = render_message

#     def first_hit(self):
#         if self.__pokemon1.get_speed() < self.__pokemon2.get_speed():
#             temp = self.__pokemon1
#             self.__pokemon1 = self.__pokemon2
#             self.__pokemon2 = temp

#     def affinity(self):
#         type_import = Type(pokemon_types, pokemon_matrice)
#         type1 = self.__pokemon1.get_types()
#         type2 = self.__pokemon2.get_types()

#         try:
#             index1 = type_import.get_types().index(type1)
#             index2 = type_import.get_types().index(type2)
#         except ValueError:
#             print(f"Erreur : Type non trouvé dans la matrice d'affinité - Type1: {type1}, Type2: {type2}")
#             return None
#         affinity_value = float(type_import.get_matrice()[index1][index2])
#         self.set_affinity_values(affinity_value)
#         if self.__affinity_values < 1:
#             self.__render_message = f"{self.__pokemon1.get_name()} lance une attaque. C'est ne pas très efficace."
#         elif self.__affinity_values == 1:
#             self.__render_message = f"{self.__pokemon1.get_name()} lance une attaque"
#         elif self.__affinity_values > 1 :
#             self.__render_message = f"{self.__pokemon1.get_name()} lance une attaque, C'est très efficace"


#         return affinity_value


#     def attack_chance(self):
#         attack_chance = random.randint(0, 100)
#         if attack_chance <= 15 :
#             # attack missed
#             self.set_attack_chance_ratio(0)
#             self.__render_message = f"L'attaque de {self.__pokemon1.get_name()} à échoué"
#         elif 16 <= attack_chance <= 90:
#             # attack hit
#             self.set_attack_chance_ratio(1)
#             self.__render_message = f"L'attaque de {self.__pokemon1.get_name()} à réussi"
#         else:
#             # attack critical hit
#             self.set_attack_chance_ratio(2)
#             self.__render_message(f"L'attaque de {self.__pokemon1.get_name()} est un coup critique")

#     def calculate_damage(self):
#         puissance_attaque = float(self.__pokemon1.get_power_attack() - self.__pokemon2.get_defense())
#         affinity_value = self.affinity()
#         damage = puissance_attaque * affinity_value
#         if damage < 1:
#             damage = 1
#         return damage
        
#     def pv_remaining(self):
#         damage = self.calculate_damage()
#         self.__pokemon2.set_pv(self.__pokemon2.get_pv() - damage)
      
#     def attack(self):
#         if self.get_attack_chance_ratio() == 1:
#             self.pv_remaining()
#         elif self.get_attack_chance_ratio() == 2:
#             damage = self.calculate_damage() * 1.5
#             self.__pokemon2.set_pv(self.__pokemon2.get_pv() - damage)

#     def level_up(self, pokemon):
#         pokemon.set_level(pokemon.get_level() + 1)
#         pokemon.set_power_attack(pokemon.get_power_attack() + 1)
#         pokemon.set_defense(pokemon.get_defense() + 1)
#         pokemon.set_speed(pokemon.get_speed() + 1)
#         pokemon.set_pv_max(pokemon.get_pv_max() + 1)
#         pokemon.set_pv(pokemon.get_pv() + 1)
#         pokemon.set_xp(0)
#         pokemon.set_xp_max(int(pokemon.get_xp_max() * 1.75))
#         self.__render_message = f"{self.__pokemon2.get_name()} est K.O. Félication {self.__pokemon1.get_name()} est passé lvl {self.__pokemon1.get_level()} et son xp est {self.__pokemon1.get_xp()} / {self.__pokemon1.get_xp_max()}"

#     def gain_xp(self):
#         if self.__pokemon2 != self.__pokemon_player:
#             self.__pokemon1.set_xp(self.__pokemon1.get_xp() + 100)
#             self.__render_message = f"{self.get_pokemon2().get_name()} est K.O. Félication {self.get_pokemon1().get_name()} est passé lvl {self.get_pokemon1().get_level()} et son xp est {self.get_pokemon1().get_xp()} / {self.get_pokemon1().get_xp_max()}"
#             if self.__pokemon1.get_xp() >= self.__pokemon1.get_xp_max():
#                 self.level_up(self.__pokemon1)
#                 return True
#             return False
                
#     # def end_game(self):
#     #     if self.__pokemon2.get_pv() <= 0 and self.__pokemon_list_2 == []:
#     #         self.gain_xp()
#     #         return self.__pokemon1.get_name()
#     #     else:
#     #         return self.__pokemon1.get_name()
#     def end_game(self):
#         if self.__pokemon2.get_pv() <= 0:
#             return True
#         return False

#     def winner_pokemon(self):
#         if self.__pokemon2.get_pv() <= 0:
#             self.gain_xp()
#             return self.__pokemon1.get_name()
#         else:
#             return self.__pokemon1.get_name()

#     # def winner_trainer(self):
#     #     if self.pokemon1.get_pv() <= 0:
#     #         return "Player 1 loses"
#     #     elif self.pokemon2.get_pv() <= 0:
#     #         return "Player 1 wins"
#     #     else:
#     #         return "Continue"

#     def end_attack(self):
#         temp = self.__pokemon1
#         self.__pokemon1 = self.__pokemon2
#         self.__pokemon2 = temp

import random
from .Pokemon import *
from graphics.graphics_attributes import *

class Combat:
    def __init__(self, pokemon1, pokemon2, attack_chance_ratio, affinity_values, player_list, computer_list, states):
        self.__pokemon_player = pokemon1
        self.__pokemon_computer = pokemon2
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2
        self.__attack_chance_ratio = attack_chance_ratio
        self.__affinity_values = affinity_values
        self.__player_list = player_list
        self.__computer_list = computer_list
        self.__states = states

    def get_pokemon_player(self):
        return self.__pokemon_player
    def set_pokemon_player(self, pokemon1):
        self.__pokemon_player = pokemon1

    def get_pokemon1(self):
        return self.__pokemon1
    def set_pokemon1(self, pokemon1):
        self.__pokemon1 = pokemon1

    def get_pokemon2(self):
        return self.__pokemon2

    def set_pokemon2(self, pokemon2):
        self.__pokemon2 = pokemon2

    def get_attack_chance_ratio(self):
        return self.__attack_chance_ratio
    def set_attack_chance_ratio(self, attack_chance_ratio):
        self.__attack_chance_ratio = attack_chance_ratio
    
    def get_affinity_values(self):
        return self.__affinity_values
    def set_affinity_values(self, affinity_values):
        self.__affinity_values = affinity_values
    
    def get_player_list(self):
        return self.__player_list
    def set_player_list(self, player_list):
        self.__player_list = player_list

    def get_computer_list(self):
        return self.__computer_list
    def set_computer_list(self, computer_list):
        self.__computer_list = computer_list

    def get_states(self):
        return self.__states
    def set_states(self, states):
        self.__states = states

    def first_hit(self):
        if self.__pokemon1.get_speed() < self.__pokemon2.get_speed():
            temp = self.__pokemon1
            self.__pokemon1 = self.__pokemon2
            self.__pokemon2 = temp

    def affinity(self):
        type_import = Type(pokemon_types, pokemon_matrice)
        type1 = self.__pokemon1.get_types()
        type2 = self.__pokemon2.get_types()

        try:
            index1 = type_import.get_types().index(type1)
            index2 = type_import.get_types().index(type2)
        except ValueError:
            print(f"Erreur : Type non trouvé dans la matrice d'affinité - Type1: {type1}, Type2: {type2}")
            return None
        affinity_value = float(type_import.get_matrice()[index1][index2])
        self.set_affinity_values(affinity_value)

        return affinity_value


    def attack_chance(self):
        attack_chance = random.randint(0, 100)
        if attack_chance <= 15 :
            # attack missed
            self.set_attack_chance_ratio(0)
        elif 16 <= attack_chance <= 90:
            # attack hit
            self.set_attack_chance_ratio(1)
        else:
            # attack critical hit
            self.set_attack_chance_ratio(2)

    def calculate_damage(self):
        puissance_attaque = float(self.__pokemon1.get_power_attack() - self.__pokemon2.get_defense())
        affinity_value = self.affinity()
        damage = puissance_attaque * affinity_value
        if damage < 1:
            damage = 1
        return damage
        
    def pv_remaining(self):
        damage = self.calculate_damage()
        self.__pokemon2.set_pv(self.__pokemon2.get_pv() - damage)
      
    def attack(self):

        if self.get_attack_chance_ratio() == 1:
            self.pv_remaining()
        elif self.get_attack_chance_ratio() == 2:
            damage = self.calculate_damage() / 0.5
            self.__pokemon2.set_pv(self.__pokemon2.get_pv() - damage)

    def level_up(self, pokemon):
        pokemon.set_level(pokemon.get_level() + 1)
        pokemon.set_power_attack(pokemon.get_power_attack() + 1)
        pokemon.set_defense(pokemon.get_defense() + 1)
        pokemon.set_speed(pokemon.get_speed() + 1)
        pokemon.set_pv_max(pokemon.get_pv_max() + 1)
        pokemon.set_pv(pokemon.get_pv() + 1)
        pokemon.set_xp(self.__pokemon1.get_xp() - self.__pokemon1.get_xp_max())
        pokemon.set_xp_max(int(pokemon.get_xp_max() * 1.75))

    def gain_xp(self):
        if self.__pokemon2 != self.__pokemon_player:
            self.__pokemon1.set_xp(self.__pokemon1.get_xp() + 100)
            if self.__pokemon1.get_xp() >= self.__pokemon1.get_xp_max():
                self.level_up(self.__pokemon1)
                return True
            return False
                
    # def end_game(self):
    #     if self.__pokemon2.get_pv() <= 0 and self.__pokemon_list_2 == []:
    #         self.gain_xp()
    #         return self.__pokemon1.get_name()
    #     else:
    #         return self.__pokemon1.get_name()
    def end_game(self):
        if self.__pokemon2.get_pv() <= 0:
            return True
        return False

    def winner_pokemon(self):
        if self.__pokemon2.get_pv() <= 0:
            self.gain_xp()
            return self.__pokemon1.get_name()
        else:
            return self.__pokemon1.get_name()

    # def winner_trainer(self):
    #     if self.pokemon1.get_pv() <= 0:
    #         return "Player 1 loses"
    #     elif self.pokemon2.get_pv() <= 0:
    #         return "Player 1 wins"
    #     else:
    #         return "Continue"

    def end_attack(self):
        temp = self.__pokemon1
        self.__pokemon1 = self.__pokemon2
        self.__pokemon2 = temp

