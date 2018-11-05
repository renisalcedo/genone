class Status:
    def __init__(self):
        # Initial Stats Properties
        self.stats = {'hp': 250, 'atk': 5, 'agi': 5, 'vit': 5, 'dex': 5, 'luk': 5, 'int': 5}

    def stat_assign(self, stat, val):
        self.stats[stat] += val

class Character(Status):
    def __init__(self, name):
        # Initial Char Properties
        self.name = name
        self.lv = 1
        self.statpoints = 0
        self.progress = 0
        self.skill_points = 0

        # Initialize Status
        Status.__init__(self)

    def receive_exp(self, lv):
        exp = (self.lv + lv) * 10
        return self.lvup(exp)

    def lvup(self, exp):
        self.progress += exp

        # When Progress is 100% lv up player
        if self.progress >= 100:
            self.stats['hp'] = 250
            self.lv += 1
            self.statpoints += 5
            self.skill_points += 2
            self.progress = 0
            print("Congrats! On Your New Lv Up \n")

    def die(self):
        print("{} just died!".format(self.name))
        return True

    def stat_helper(self, stat, val):
        if self.statpoints > 0 and val <= self.statpoints:
            self.stat_assign(stat, val)
            self.statpoints -= val
        else:
            print("Status points available: ", self.statpoints)

    def stat_menu(self):
        print("HP: {} \n ATK: {} \n AGI: {} \n VIT: {} \n DEX: {} \n LUK: {} \n INT: {} \n".format(
            self.get_stat('hp'), self.get_stat('atk'), self.get_stat('agi'), self.get_stat('vit'),
            self.get_stat('dex'), self.get_stat('dex'), self.get_stat('luk'), self.get_stat('int')
        ))

        stat = input("Select status: ")
        val = int(input("Select Status level: "))

        self.stat_helper(stat, val)

    def get_stat(self, stat):
        return self.stats[stat]