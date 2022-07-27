from game_logic import GameLogic

class Game:
    def __init__(self):
        pass

    @staticmethod
    def play_game(dice_roller):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == "n":
            print("OK. Maybe another time")

        elif response == "y":
            # track number of rounds played
            rounds = 1
            # start game
            while rounds < 20:
                print(f"Starting round {rounds}")
                while True:
                    print("Rolling 6 dice...")
                    # roll 6 dice
                    roll = dice_roller(6)
                    # format roll info
                    roll_values = []
                    for val in roll:
                        roll_values.append(str(val))
                    formatted_roll = " ".join(roll_values)
                    # display rolls
                    print(f"*** {formatted_roll} ***")
                    print("Enter dice to keep, or (q)uit:")
                    keep = input("> ")
                    if keep == "q":
                        print("Thanks for playing. You earned 0 points")
                        return "quit"

                    shelf = Game.dice_shelf(keep)

                    print(f"You have 50 unbanked points and {shelf[1]} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    choice = input("> ")
                    print(f"You banked 50 points in round {rounds}")
                    print("Total score is 50 points")
                    break
                rounds += 1

    if __name__ == "__main__":
        play_game(roll_dice)