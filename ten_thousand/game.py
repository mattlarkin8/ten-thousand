from game_logic import GameLogic, Banker

def play(roller=GameLogic.roll_dice, num_rounds=20):
    choice = ask_to_play()
    if choice == "y":
        start_game(num_rounds)
    else:
        decline_game()

def ask_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    return input("> ")

def start_game(num_rounds):
    # track rounds played
    round_count = 1
    # run game for given number of rounds
    while round_count <= num_rounds:
        round_result = do_round(round_count)
        if round_result == "q":
            break

        round_count += 1

    print(f"Thanks for playing. You earned {Banker.get_score()} points")

def do_round(round_count):
    start_round(round_count)
    # track points for this round
    round_points = 0
    # create clean starting point for new round
    num_dice = 6
    # start the player turn action loop for this round
    turn_results = play_turn(num_dice)
    # add turn points to the total points for this round
    round_points += turn_results

    if turn_results == -1:
        return "q"

    print(f"You banked {round_points} points in round {round_count}")
    Banker.add_to_score(round_points)
    print(f"Total score is {Banker.get_score()} points")

    return round_points

def play_turn(num):
    num_dice = num
    keepers = []
    turn_points = 0
    while True:
        # roll remaining dice
        roll = roll_dice(num_dice)
        # display the results of the roll
        print(f"*** {format_roll(roll)} ***")

        # check if roll is zilch
        if GameLogic.calculate_score(roll) == 0:
            zilch()
            return 0

        # prompt user to keep dice
        print("Enter dice to keep, or (q)uit:")
        keep = input("> ")
        # check if user quit
        if keep == "q":
            return -1

        # verify that user input is valid


        # keep selected dice
        new = GameLogic.dice_shelf(keep)
        for num in new:
            keepers.append(num)
        # update number of remaining dice
        num_dice = 6 - len(keepers)

        # score kept dice
        points = GameLogic.calculate_score(new)

        # hot dice - if all dice score, refresh dice
        if num_dice == 0:
            turn_points += points
            keepers = []
            num_dice = 6

        if num_dice < 6:
            # update points earned this turn
            turn_points += points

        print(f"You have {turn_points} unbanked points and {num_dice} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        choice = input("> ")
        if choice == "q":
            return -1

        if choice == "b":
            return turn_points

def roll_dice(num_dice):
    print(f"Rolling {num_dice} dice...")
    return GameLogic.roll_dice(num_dice)

def add_to_shelf(keep):
    return GameLogic.dice_shelf(keep)

def format_roll(roll):
    roll_values = []
    for val in roll:
        roll_values.append(str(val))
    formatted_roll = " ".join(roll_values)
    return formatted_roll

def start_round(round_count):
    print(f"Starting round {round_count}")

def zilch():
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")

def decline_game():
    print("OK. Maybe another time")

def quit_game():
    print(f"Thanks for playing. You earned {Banker.get_score()} points")

if __name__ == '__main__':
    play()