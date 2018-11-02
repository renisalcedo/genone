class Status:
    def __init__(self):
        # Initial Stats Properties
        self.stats = {'hp': 1500, 'atk': 5, 'agi': 5, 'vit': 5, 'dex': 5, 'luk': 5}

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

    def lvup(self, exp):
        self.progress += exp

        # When Progress is 100% lv up player
        if self.progress >= 100:
            self.lv += 1
            self.statpoints += 5
            self.skill_points += 2
            self.progress = 0
            print("Congrats! On Your New Lv Up \n")

    def die(self):
        print("{} just died!".format(self.name))
        return True

    def stat_helper(self, stat, val):
        if self.statpoints > 0:
            self.stat_assign(stat, val)
        else:
            print("Status points available: ", self.statpoints)

    def get_stat(self, stat):
        return self.stats[stat]