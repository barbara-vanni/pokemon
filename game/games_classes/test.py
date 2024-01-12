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

            if self.attack_chance() == 0:
                print("Attack missed")
            elif self.attack_chance() == 1:
                print("Attack hit")
                defender.pv = self.pv_remaining(attacker, defender)
            else:
                print("Critical hit")
                damage = self.calculate_damage(attacker, defender) * 0.5
                pv_remaining = defender.set_pv(defender.get_pv() - damage)
                defender.pv = self.pv_remaining(attacker, defender)



    def calculate_damage(self, attacker, defender):
        affinity_values = self.affinity(attacker)
        ratio_affinity = float(affinity_values)
        puissance_attaque = float(attacker.get_power_attack() - defender.get_defense())
        damage = puissance_attaque * ratio_affinity
        if damage < 1:
            damage = 1
        return float(damage)



    def pv_remaining(self, attacker, defender):
        damage = self.calculate_damage(attacker, defender)
        pv_remaining = defender.set_pv(defender.get_pv() - damage)
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
            return "Player 1 loses"
        elif self.pokemon2.get_pv() <= 0:
            return "Player 1 wins"
        else:
            return "Continue"



    def gain_xp(self, attacker, defender):
        if self.pokemon1.get_pv() <= 0:
            xp_gain = self.pokemon2.set_xp(self.pokemon2.get_xp() + 100)
        elif self.pokemon2.get_pv() <= 0:
            xp_gain = self.pokemon1.set_xp(self.pokemon1.get_xp() + 100)
        else:
            xp_gain = "Continue"
        return xp_gain


    # def level_xp(self):
    #     if self._xp >= self._xp_max:
    #         self._level += 1
    #         self._xp = 0
    #         self._xp_max = int(self._xp * 1.75)
    #         print(f"Level up ! Level : {self._level}")

    def level_up(self):
        if self._xp >= self._xp_max:
            self.set_level(self.get_level() + 1)
            self._power_attack += 1
            self._defense += 1
            self._speed += 1
            self._pv += 1
            print(f"{self._name} leveled up to Level {self._level}!")
        else:
            pass

    # def level_up(self):
    #     self.set_level(self.get_level() + 1)
    #     self._power_attack += 1
    #     self._defense += 1
    #     self._speed += 1
    #     self._pv += 1
    #     print(f"{self._name} leveled up to Level {self._level}!")



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
            print(f"{attacker.get_name()}: {attacker.get_pv()} PV VS {defender.get_name()}: {defender.get_pv()} PV")
            print("Fight!\n")

            while attacker.get_pv() > 0 and defender.get_pv() > 0:

                choice = input("Choose attack : yes/no")

                self.attack(attacker, defender)
                print(f"{attacker.get_name()} attacks {defender.get_name()}")
                # self.pv_remaining(attacker, defender)
                print(f"{defender.get_name()} has {defender.get_pv()} PV ")
                attacker, defender = self.end_attack(attacker, defender)
                winner_pokemon = self.winner_pokemon()
                winner_trainer = self.winner_trainer()
                if defender.get_pv() <= 0 or attacker.get_pv() <= 0:
                    if self.end_game() == "You lose":
                        return f"{self.winner_pokemon()}\n {self.winner_trainer()}"
                    elif self.end_game() == "You win":
                        xp_gain = self.gain_xp(attacker, defender)

                        return f"{winner_pokemon}\n{winner_trainer}\n{winner_pokemon} has {self.pokemon1.get_xp()} xp"



                self.attack(attacker, defender)
                print(f"{attacker.get_name()} attacks {defender.get_name()}")
                # self.pv_remaining(attacker, defender)
                print(f"{defender.get_name()} has {defender.get_pv()} PV \n")
                attacker, defender = self.end_attack(attacker, defender)
                winner_pokemon = self.winner_pokemon()
                winner_trainer = self.winner_trainer()
                if defender.get_pv() <= 0 or attacker.get_pv() <= 0:
                    if self.end_game() == "You lose":
                        return f"{self.winner_pokemon()}\n {self.winner_trainer()}"
                    elif self.end_game() == "You win":
                        xp_gain = self.gain_xp(attacker, defender)
                        return f"{winner_pokemon}\n{winner_trainer}\n{winner_pokemon} has {self.pokemon1.get_xp()} xp"



        elif answer == "no":
            return "You lose"
        else:
            #print("Type yes or no")
            return self.fight()

combat = Combat(pokemon1, pokemon2)



# print(f"{combat.affinity()} hahaha")
# print("pv", combat.pokemon1.get_pv())
# print("pv", combat.pokemon2.get_pv())
# # print(combat.end_game())
# print(combat.winner_trainer())
print(combat.fight())
print(Pokemon.informations_pokemon(pokemon1))
print(combat.fight())
