import random
from Pokemon import weakness_resistance1, weakness_resistance2, pokemon1, pokemon2, Pokemon
from Type import *

class Combat:
    def __init__(self, attacker, defenser):
        self.pokemon1 = attacker
        self.pokemon2 = defenser

    def first_hit(self):
        if self.pokemon1.speed > self.pokemon2.speed:
            first_hit = self.pokemon1
        elif self.pokemon1.speed < self.pokemon2.speed:
            first_hit = self.pokemon2
        else:
            first_hit = random.choice([self.pokemon1, self.pokemon2])
        return first_hit


    def affinity(self):
        affinity_values1 = weakness_resistance1
        affinity_values2 = weakness_resistance2
        return affinity_values1, affinity_values2   

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





    def calculate_damage(self, attacker):
        affinity_values1, affinity_values2 = self.affinity()
        ratio_affinity1 = float(affinity_values1)
        puissance_attaque1 = float(self.pokemon1.get_power_attack())
        damage1 = puissance_attaque1 * ratio_affinity1

        ratio_affinity2 = float(affinity_values2)
        puissance_attaque2 = float(self.pokemon2.get_power_attack())
        damage2 = puissance_attaque2 * ratio_affinity2

        return float(damage1), float(damage2)


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
            print(f"{attacker.get_name()} VS {defender.get_name()}")
            print("Fight!")

            while attacker.get_pv() > 0 and defender.get_pv() > 0:
                print(f"{attacker.get_name()} attacks {defender.get_name()}")

                damage = self.calculate_damage(attacker)
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


combat = Combat(pokemon1, pokemon2)



# print(f"{combat.affinity()} hahaha")
# print("pv", combat.pokemon1.get_pv())
# print("pv", combat.pokemon2.get_pv())
# print(combat.end_game())
# print(combat.winner_trainer())
print(combat.affinity())
print(combat.fight())