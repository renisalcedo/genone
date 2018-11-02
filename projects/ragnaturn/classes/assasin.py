from .util.character import Character
from random import randint

class Assasin(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        self.skill_lv = {'double_attack': 0, 'sonic_blow': 0, 'meteor_assault': 0, 'hide': 0} 

    def double_attack(self):
        atk = self.get_stat('atk')
        dmg = atk * 2

        print("Double Attack!! DMG: ", dmg)

        return dmg

    def sonic_blow(self):
        atk = self.get_stat('atk')
        dex = self.get_stat('dex')
        dmg = atk * dex
        total_dmg = 0

        for _ in range(10):
            total_dmg += dmg
            print("Sonic Blow!! DMG ", dmg)

        return total_dmg

    def meteor_assault(self):
        atk = self.get_stat('atk')
        vit = self.get_stat('vit')
        dex = self.get_stat('dex')

        dmg = atk * (vit + dex)

        print("METEOR ASSAULT! DMG ", dmg)

        return dmg

    def choose_attack(self, id):
        if id == 1:
            return self.double_attack()
        elif id == 2:
            return self.sonic_blow()
        else:
            return self.meteor_assault()

    def skills_menu(self):
        print("Skills Menu ...")
        print("1) Double Attack")
        print("2) Sonic Blow")
        print("3) Meteor Assault")

        id = int(input("Choose Attack!"))
        return self.choose_attack(id)

    def automate(self):
        skill = randint(1, 3)

        return self.choose_attack(skill)

    def receive_dmg(self, dmg):
        if dmg:
            print("{} was attacked! with DMG {}!".format(self.name, dmg))
            self.stats['hp'] -= dmg

        if self.get_stat('hp') <= 0:
            return self.die()