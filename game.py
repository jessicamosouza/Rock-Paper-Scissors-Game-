import random


class Game:
    def start(self):
        self.choices = ['r', 'p', 's']

        user_input = input(
            "Press 'r' for rock, 'p' for paper or 's' for scissors: ").lower()
        if not self.is_input_valid(user_input):
            print("Input invalid. Try again.")
            self.start()
            return

        comp_input = random.choice(self.choices)
        user_won = self.did_user_win(comp_input, user_input)
        self.print_winner(user_won, comp_input)

    def is_input_valid(self, user_input):
        for i in range(len(self.choices)):
            if user_input == self.choices[i]:
                return True
        return False

    def did_user_win(self, comp, user):
        if comp == user:
            return

        elif comp == 'p':
            return user != 'r'

        elif comp == 'r':
            return user != 's'

        elif comp == 's':
            return user != 'p'

    def print_winner(self, result, comp_chose):
        if result:
            print(f"You won! Computer chose: {comp_chose}")

        elif result == False:
            print(f"You lost! Computer chose: {comp_chose}")

        else:
            print("Tied. Play again.")
            self.start()


game = Game()
game.start()
