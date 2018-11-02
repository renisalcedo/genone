from interface import Interface
from time import sleep

class Game:
    def __init__(self):
        self.playing = True
        self.player = None
        self.enemy = None

    def create(self):
        # PLAYER SETUP
        screen = Interface()
        screen.main_menu()

        # Get the player
        self.player = screen.get_player()

        # ENEMY SETUP
        enemy_screen = Interface()
        enemy_screen.main_menu()

        # GET THE ENEMY
        self.enemy = enemy_screen.get_player()

    def update(self):
        while self.playing:
            # CURRENT STATUS
            print("{} HP: {} \n".format(self.player.name, self.player.get_stat('hp')))
            print("{} HP: {} \n".format(self.enemy.name, self.enemy.get_stat('hp')))

            # PLAYER's TURN
            dmg = self.player.skills_menu()
            died = self.enemy.receive_dmg(dmg)

            if died:
                print("PLAYER WINS!")
                break

            sleep(1)

            # ENEMY's TURN
            enemy_dmg = self.enemy.automate()
            died = self.player.receive_dmg(enemy_dmg)

            if died:
                print("Enemy Wins!")
                break

    def main(self):
        self.create()
        self.update()

game = Game()
game.main()