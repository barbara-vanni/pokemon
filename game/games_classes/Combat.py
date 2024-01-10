import random
from Pokemon import weakness_resistance, pokemon1, pokemon2, Pokemon
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
        affinity_values = weakness_resistance
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
    
    def attack(self, attacker, defender):
        if button_attack.is_pressed:
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
    
    def gain_xp(self):
        if self.pokemon1.get_pv() <= 0:
            return self.pokemon2.set_xp + 100
        elif self.pokemon2.get_pv() <= 0:
            return self.pokemon1.set_xp + 100
        else:
            return "Continue"
    
    def level_up(self):
        if self.pokemon1.get_pv() <= 0:
            return self.pokemon2.set_level + 1
        elif self.pokemon2.get_pv() <= 0:
            return self.pokemon1.set_level + 1
        else:
            return "Continue"

combat = Combat(pokemon1, pokemon2)



print(f"{combat.affinity()} hahaha")
print("pv", combat.pokemon1.get_pv())
print("pv", combat.pokemon2.get_pv())
print(combat.end_game())
print(combat.winner_game())