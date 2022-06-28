import random


class Game:
    def __init__(self):
        self.choices = ['r', 'p', 's']

    # get user input
    def input(self):
        self.user = input(
            "Press 'r' for rock, 'p' for paper or 's' for scissors: ")
        self.user = self.user.lower()
        print("user chose: ", self.user)  # test

    # check user input
    def check_input(self):
        for i in range(len(self.choices)):
            if self.user == self.choices[i]:
                print("Correct input")  # meu
                return i
        print("Incorrect input. Try again.")
        game.input()

    # get computer random input

    def computer(self):
        self.comp_input = random.choice(self.choices)

        print(self.comp_input)

        return self.comp_input

    def check_winner(self):
        if self.comp_input != self.user:
            if self.comp_input == 'p':
                if self.user == 'r':
                    return 'l'
                else:
                    return 'w'

            elif self.comp_input == 'r':
                if self.user == 's':
                    return 'l'
                else:
                    return 'w'

            elif self.comp_input == 's':
                if self.user == 'p':
                    return 'l'
                else:
                    return 'w'

        else:
            return 't'

game = Game()

game.input()
game.check_input()
game.computer()
check_winner = game.check_winner()
game.print_winner()
