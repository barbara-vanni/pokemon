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
        affinity_values = self.weakness_resistance(pokemon1, pokemon2, attacker)
        return affinity_values
    
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
    
    # def attack(self, attacker, defender):
    #     if button_attack.is_pressed:
    #         print("You choose attack")
    #         if self.attack_chance() == 0:
    #             print("Attack missed")
    #         elif self.attack_chance() == 1:
    #             print("Attack hit")
    #             defender.pv = self.pv_remaining(attacker, defender)
    #             print("Remaining PV : ", defender.pv)
    #         else:
    #             print("Critical hit")
    #             defender.pv = self.pv_remaining(attacker, defender)
    #             print("Remaining PV : ", defender.pv)

        


    
    def calculate_damage(self,attacker):
        damage = self.power_attack * self.affinity_values
        return damage
    
    def pv_remaining(self, pokemon1, pokemon2):
        pv_remaining = pokemon2.pv - self.calculate_damage(pokemon1)
        return pv_remaining
    
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
    
    
    def ratio_xp(self):	
        pass

    def gain_xp(self):
        if self.pokemon1.get_pv() <= 0:
            return self.pokemon2.set_xp + 100
        elif self.pokemon2.get_pv() <= 0:
            return self.pokemon1.set_xp + 100
        else:
            return "Continue"
    
    def level_up(self):
        if self.pokemon1.get_xp() >= 100:
            return self.pokemon1.set_level + 1
        elif self.pokemon2.get_xp() >= 100:
            return self.pokemon2.set_level + 1
        else:
            return "Continue"

    def fight(self):
        attacker, defender = self.first_hit()
        print("The battle is going to begin! Would you want to fight?  (yes/no)")
        answer = input()

        if answer == "yes":
            print("Let's go!")
        
            print(f"{self.pokemon1.get_name()} VS {self.pokemon2.get_name()}")
            print("Fight!")

            while self.pokemon1.get_pv() > 0 and self.pokemon2.get_pv() > 0:
                print(f"{self.pokemon1.get_name()} attacks {self.pokemon2.get_name()}")
                self.pokemon2.set_pv(self.pokemon2.get_pv() - self.pokemon1.get_power_attack())
                print(f"{self.pokemon2.set_pv(self.pokemon2.get_pv() - self.pokemon1.get_power_attack())}, \n")

                print(f"{self.pokemon2.get_name()} has {self.pokemon2.get_pv()} PV left")
                print(f"{self.pokemon2.get_name()} attacks {self.pokemon1.get_name()}")
                self.pokemon1.set_pv(self.pokemon1.get_pv() - self.pokemon2.get_power_attack())
                print(f"{self.pokemon1.get_name()} has {self.pokemon1.get_pv()} PV left")
            if self.pokemon1.get_pv() <= 0:
                winner = f"{self.pokemon2.get_name()} is the winner"
            elif self.pokemon2.get_pv() <= 0:
                winner = f"{self.pokemon1.get_name()} is the winner"
            else:
                winner = "Continue"
                return winner
        
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

