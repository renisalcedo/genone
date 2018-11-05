from classes.orc import Orc
from interface import Interface
from time import sleep

class Game:
    def __init__(self):
        self.playing = True
        self.player = None
        self.enemy = None
        self.enemies_num = 20

    def create(self):
        # PLAYER SETUP
        screen = Interface()
        screen.main_menu()

        # Get the player
        self.player = screen.get_player()

        # ENEMY SETUP
        self.enemy = Orc()

    def adventure(self):
        # HP FOR ENEMY AND PLAYER
        print("{} HP: {} \n".format(self.player.name, self.player.get_stat('hp')))
        print("{} HP: {} \n".format(self.enemy.name, self.enemy.get_stat('hp')))

        enemy_died = False

        # No More enemies alive
        if self.enemies_num == 0:
            return "Mission Completed!"

        # Play Adventure
        # USER TURN
        dmg = self.player.skills_menu()
        enemy_died = self.enemy.receive_dmg(dmg)

        # One Enemy Died
        if enemy_died:
            self.enemies_num -= 1
            print("You Eliminated one Enemy!")
            print("Remaining Enemies in room: {}".format(self.enemies_num))

            # User receive xp
            self.player.receive_exp(self.enemy.lv)
            print("PROGRESS: {}".format(self.player.progress))

            while self.player.statpoints > 0 or self.player.skill_points > 0:
                if self.player.statpoints > 0:
                    print("Available Status Points: {}".format(self.player.statpoints))
                    self.player.stat_menu()

                if self.player.skill_points > 0:
                    print("Available Skills Points: {}".format(self.player.skill_points))
                    self.player.skill_menu()

            # Recreate new enemy
            self.enemy = Orc()

        # Enemy Turn
        enemy_dmg = self.enemy.automate()

        # User damaged!
        died = self.player.receive_dmg(enemy_dmg)

        if died:
            self.playing = False

    def update(self):
        while self.playing:
            self.adventure()
            
    def main(self):
        self.create()
        self.update()

game = Game()
game.main()