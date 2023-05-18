from collections import Counter
from Game import Game


def get_user_menu_choice():
    while True:
        print("\n--- Menu ---")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")

        choice = input("Please enter your choice (1/2/3): ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def print_results(results):
    print("\n--- Game Results ---")
    if results:
        print("Total games played:", sum(list(results.values())))
        print("Wins:", results["win"])
        print("Losses:", results["loss"])
        print("Draws:", results["draw"])
    else:
        print("No games played.")
    print("Thank you for playing!")


def main():
    game_results = Counter({"win": 0, "draw": 0, "loss": 0})
    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            result = game.play()
            if result == "win":
                game_results["win"] += 1
            elif result == "loss":
                game_results["loss"] += 1
            else:
                game_results["draw"] += 1
        elif choice == "2":
            print_results(game_results)
        else:
            print_results(game_results)
            break


main()
