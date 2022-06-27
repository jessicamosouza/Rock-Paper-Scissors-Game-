class User:
    def get_user_input(self, choices):
        user_input = input(
            "Press 'r' for rock, 'p' for paper or 's' for scissors: ")
        print("user chose: ", user_input)  # test

        print(len(choices))
