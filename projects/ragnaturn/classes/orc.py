from random import randint
from .util.character import Character

class Orc(Character):
    def __init__(self):
        Character.__init__(self, "Orc")

        # Skills by lv
        self.skill_lv = {'bash': 1, 'shield_charge': 1, 'fire_attack': 1}

    def bash(self):
        atk = self.get_stat('atk')
        dmg = atk*2

        print("Bash! dmg: {}".format(dmg))
        return dmg

    def shield_charge(self):
        atk = self.get_stat('atk')
        dex = self.get_stat('dex')

        dmg = (atk * dex) * 2
        print("Shield Charge DMG: {}".format(dmg))

        return dmg

    def fire_attack(self):
        inteligence = self.get_stat('int')

        dmg = (inteligence * 3) * self.skill_lv['fire_attack']
        print("Fire Attack DMG: {}".format(dmg))

        return dmg

    def choose_skill(self, key):
        if key == 1:
            return self.bash()
        elif key == 2:
            return self.fire_attack()
        elif key == 3:
            return self.shield_charge()

    def automate(self):
        skill = randint(1,3)

        return self.choose_skill(skill)

    def receive_dmg(self, dmg):
        if dmg:
            print("{} was attacked! with DMG {}!".format(self.name, dmg))
            self.stats['hp'] -= dmg

        if self.get_stat('hp') <= 0:
            return self.die()
