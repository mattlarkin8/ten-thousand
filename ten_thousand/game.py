from game_logic import GameLogic, Banker

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
                # create empty shelf for new round
                shelf = GameLogic.dice_shelf()
                print(f"Starting round {rounds}")
                while True:
                    print(f"Rolling {shelf[1]} dice...")
                    # roll remaining dice
                    roll = dice_roller(shelf[1])
                    # format roll info
                    roll_values = []
                    for val in roll:
                        roll_values.append(str(val))
                    formatted_roll = " ".join(roll_values)
                    # display rolls
                    print(f"*** {formatted_roll} ***")
                    print("Enter dice to keep, or (q)uit:")
                    keep = input("> ")
                    # check if user quit game
                    if keep == "q":
                        print(f"Thanks for playing. You earned {Banker.get_score()} points")
                        return "quit"
                    # add kept dice to shelf
                    shelf = GameLogic.dice_shelf(keep)
                    print(shelf)
                    # calculate points of dice on shelf
                    points = GameLogic.calculate_score(shelf[0])
                    print(points)
                    print(f"You have {points} unbanked points and {shelf[1]} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    choice = input("> ")
                    # check if user quit game
                    if choice == "q":
                        print(f"Thanks for playing. You earned {Banker.get_score()} points")
                        return "quit"
                    # check if user banked points
                    elif choice == "b":
                        print(f"You banked {points} points in round {rounds}")
                        Banker.add_to_score(points)
                        print(f"Total score is {Banker.get_score()} points")
                        break
                    # check if user rolled again
                    elif choice == "r":
                        continue
                rounds += 1

    if __name__ == "__main__":
        play_game(GameLogic.roll_dice)