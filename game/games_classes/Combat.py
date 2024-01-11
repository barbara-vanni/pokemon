import random
from Pokemon import pokemon1, pokemon2, Pokemon
from Type import *

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def first_hit(self):
        speed_pokemon1 = self.pokemon1.get_speed()
        speed_pokemon2 = self.pokemon2.get_speed()

        if speed_pokemon1 > speed_pokemon2:
            attacker = self.pokemon1
            defender = self.pokemon2    
        else :
            attacker = self.pokemon2
            defender = self.pokemon1
        return attacker, defender

    def affinity(self, attacker):
        type1 = self.pokemon1.get_types()
        type2 = self.pokemon2.get_types()

        type_import = Type(pokemon_types, pokemon_matrice)

        if self.pokemon1 == attacker:
            index1 = type_import.get_types().index(type1)
            index2 = type_import.get_types().index(type2)
            affinity_values = type_import.get_matrice()[index1][index2]
        elif self.pokemon2 == attacker:
            index1 = type_import.get_types().index(type2)
            index2 = type_import.get_types().index(type1)
            affinity_values = type_import.get_matrice()[index1][index2]
        else:
            affinity_values = 1

        return float(affinity_values)

    
    def attack_chance(self):
        attack_chance = random.randint(0, 100)
        if attack_chance <= 15 :
            # attack missed
            attack_chance_ratio = 0 
        elif 16 <= attack_chance <= 90:
            # attack hit
            attack_chance_ratio = 1
        else:
            # attack critical hit
            attack_chance_ratio = 2
        return attack_chance_ratio
    
    def attack(self, attacker, defender):
        choice = input("Choose attack : yes/no")

        if choice == "yes":
            print("You choose attack")
            if self.attack_chance() == 0:
                print("Attack missed")
            elif self.attack_chance() == 1:
                print("Attack hit")
                defender.pv = self.pv_remaining(attacker, defender)
                print("Remaining PV : ", defender.pv)
            else:
                print("Critical hit")
                defender.pv = self.pv_remaining(attacker, defender)
                print("Remaining PV : ", defender.pv)
    
    def calculate_damage(self, attacker, defender):
        affinity_values = self.affinity(attacker)
        ratio_affinity = float(affinity_values)
        puissance_attaque = float(attacker.get_power_attack() - defender.get_defense())
        damage = puissance_attaque * ratio_affinity
        if damage < 1:
            damage = 1
        return float(damage)
    
    def pv_remaining(self, attacker, defender):
        pv_remaining = defender.get_pv - self.calculate_damage(attacker)
        return max(pv_remaining, 0)
    
    def end_game(self):
        if self.pokemon1.get_pv() <= 0:
            return "You lose"
        elif self.pokemon2.get_pv() <= 0:
            return "You win"
        else:
            return "Continue"

    def winner_pokemon(self):
        if self.pokemon1.get_pv() <= 0:
            return f"{pokemon2.get_name()} is the winner"
        elif self.pokemon2.get_pv() <= 0:
            return f"{pokemon1.get_name()} is the winner"
        else:
            return "Continue"
    
    def winner_trainer(self):
        if self.pokemon1.get_pv() <= 0:
            return "You lose"
        elif self.pokemon2.get_pv() <= 0:
            return "You win"
        else:
            return "Continue"

    def gain_xp(self):
        if self.pokemon1.get_pv() <= 0:
            return self.pokemon2.set_xp + 100
        elif self.pokemon2.get_pv() <= 0:
            return self.pokemon1.set_xp + 100
        else:
            return "Continue"
        
    def end_attack(self, attacker, defender):
        temp = attacker
        attacker = defender
        defender = temp
        return attacker, defender

    def fight(self):
        attacker, defender = self.first_hit()
        print("The battle is going to begin! Would you want to fight?  (yes/no)")
        answer = input()

        if answer == "yes":
            print("Let's go!")
            print(f"{attacker.get_name()} VS {defender.get_name()}")
            print(f"{attacker.get_name()} has {attacker.get_pv()} PV and {defender.get_name()} has {defender.get_pv()} PV")
            print("Fight!")

            while attacker.get_pv() > 0 and defender.get_pv() > 0:
                print(f"{attacker.get_name()} attacks {defender.get_name()}")

                damage = self.calculate_damage(attacker, defender)
                defender.set_pv(defender.get_pv() - damage)
                print(f"{defender.get_name()} has {defender.get_pv()} PV ")
                attacker, defender = self.end_attack(attacker, defender)
                
                if self.pokemon1.get_pv() <= 0:
                    winner = f"{self.pokemon2.get_name()} is the winner"
                    break
                elif self.pokemon2.get_pv() <= 0:
                    winner = f"{self.pokemon1.get_name()} is the winner"
                    break
                else:
                    winner = "Continue"
                print(winner) 

        elif answer == "no":
            return "You lose"
        else:
            print("Type yes or no")
            return self.fight()
        



    # def fight(self):
    #     attacker, defender = self.first_hit()
    #     print(f"{attacker.get_name()} VS {defender.get_name()}")

    #     while attacker.get_pv() > 0 and defender.get_pv() > 0:
    #         self.attack(attacker, defender)
    #         print(f"{attacker.get_name()} attacks {defender.get_name()}")
    #         defender.set_pv(defender.get_pv() - attacker.get_power_attack())
    #         print(f"{defender.get_name()} has {max(defender.get_pv(), 0)} PV left \n")


    #         attacker, defender = self.end_attack(attacker, defender)

    #         if defender.get_pv() <= 0:
    #             break  

    #         if attacker.get_pv() <= 0:
    #             break  



combat = Combat(pokemon1, pokemon2)



# print(f"{combat.affinity()} hahaha")
# print("pv", combat.pokemon1.get_pv())
# print("pv", combat.pokemon2.get_pv())
# # print(combat.end_game())
# print(combat.winner_trainer())
print(combat.fight())
