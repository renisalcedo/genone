from classes.assasin import Assasin

class Interface:
    def __init__(self):
        self.player = None
        self.name = None

    def main_menu(self):
        self.set_name()

        # GET CLASS FOR THE USER
        self.choose_menu()
        char_class = int(input("Please, Chooose a character: "))

        # Set the Job Class for the user
        self.set_class(char_class, self.name)

    def choose_menu(self):
        print("Characters: ")
        print("1) Assasin")
        print("2) Lord Knight")
        print("3) Paladin")
        print("\n\n")

    def set_class(self, id, name):
        if id == 1:
            self.player = Assasin(name)

    def set_name(self):
        # GREET USER
        print("WELCOME TO RAGNATURN!")
        name = input("Please, tell me your name: ")

        # Set the name
        print("Hi {} !".format(name))
        self.name = name

    def get_player(self):
        return self.player