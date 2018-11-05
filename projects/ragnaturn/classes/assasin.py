from .util.character import Character
from random import randint

class Assasin(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        self.skill_lv = {'double_attack': 1, 'sonic_blow': 1, 'meteor_assault': 1} 
        self.skills = ['Double Attack', 'Sonic Blow', 'Meteor Assault']

    def double_attack(self):
        atk = self.get_stat('atk')
        dmg = atk * 2

        print("Double Attack!! DMG: ", dmg)

        return dmg

    def sonic_blow(self):
        atk = self.get_stat('atk')
        dex = self.get_stat('dex')
        dmg = atk * dex * self.skill_lv['sonic_blow']
        total_dmg = 0

        for _ in range(10):
            total_dmg += dmg
            print("Sonic Blow!! DMG ", dmg)

        return total_dmg

    def meteor_assault(self):
        atk = self.get_stat('atk')
        vit = self.get_stat('vit')
        dex = self.get_stat('dex')

        dmg = atk * (vit + dex) * self.skill_lv['meteor_assault']

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

        id = int(input("Choose Attack: "))
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

    def skill_assign(self, skill, val):
        if self.skill_points > 0 and val <= self.skill_points:
            self.skill_lv[skill] += val
            self.skill_points -= val
        else:
            print("Not enough Points!")

    def skill_menu(self):
        i = 1
        for skill in self.skills:
            skill_char = skill.split(" ")
            skill_key = "_".join(skill_char).lower()
            print(skill_key)
            print("ID: {} Skill: {} Level: {}".format(i, skill, self.skill_lv[skill_key]))
            i += 1

        skill = int(input("Choose skill ID: "))
        points = int(input("Choose points: "))

        if skill == 1:
            return self.skill_assign('double_attack', points)
        if skill == 2:
            return self.skill_assign('sonic_blow', points)
        if skill == 3:
            return self.skill_assign('meteor_assault', points)