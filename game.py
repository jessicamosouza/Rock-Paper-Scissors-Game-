class Game:
    def __init__(self):
        self.choices = ['r', 'p', 's']

    #get user input
    def input(self):
        self.user_input = input(
            "Press 'r' for rock, 'p' for paper or 's' for scissors: ")
        print("user chose: ", self.user_input)  # test
        
    # check user input
    def check_input(self):
        for i in range(len(self.choices)):
            if self.user_input == self.choices[i]:
                print("Correct input")  # meu
                return i
        print("Incorrect input. Try again.")
        game.input()
        game.check_input()


game = Game()
game.input()
game.check_input()
