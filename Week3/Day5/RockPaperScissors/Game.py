import random


class Game:
    def get_user_item(self):
        while True:
            user_item = input(
                "Please select an item ((r)ock/(p)aper/(s)cissors): ").lower()
            if user_item in ["r", "p", "s"]:
                return user_item
            else:
                print("Invalid selection. Please try again.")

    def get_computer_item(self):
        options = ["r", "p", "s"]
        return random.choice(options)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "tie"
        elif (user_item == "p" and computer_item == "r") or (user_item == "s" and computer_item == "p") or (user_item == "r" and computer_item == "s"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"you have selected: {user_item}")
        print(f"the computer has selected: {computer_item}")

        if (result == 'draw'):
            print("you have both selected the same,its a tie")
        elif (result == 'win'):
            print("you won this game")
        else:
            print("the computer won you lost this time")

        return result
