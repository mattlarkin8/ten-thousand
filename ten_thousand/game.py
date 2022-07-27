from game_logic import GameLogic, Banker

def play():
    choice = ask_to_play()
    if choice == "y":
        start_game()
    else:
        decline_game()

def ask_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    return input("> ")

def decline_game():
    print("OK. Maybe another time")

def start_game():
    rounds = 1
    max_round = 20
    while rounds <= max_round:
        round_result = do_round(rounds)
        if round_result == "q":
            break

        rounds += 1

    print(f"Thanks for playing. You earned {Banker.get_score()} points")

def quit_game():
    print(f"Thanks for playing. You earned {Banker.get_score()} points")

def do_round(rounds):
    start_round(rounds)
    # track points for this round
    round_points = 0
    # create clean dice shelf to start round
    shelf = GameLogic.dice_shelf()
    # start the player turn action loop for this round
    turn_results = play_turn(shelf)
    # capture return values needed for further action
    choice = turn_results[0]
    turn_points = turn_results[1]
    # add turn points to the total points for this round
    round_points += turn_points
    if choice == "q":
        return "q"
    elif choice == "b":
        print(f"You banked {round_points} points in round {rounds}")
        Banker.add_to_score(round_points)
        print(f"Total score is {Banker.get_score()} points")

    return round_points

def play_turn(shelf):
    while True:
        print(f"Rolling {shelf[1]} dice...")
        roll = roll_dice(shelf[1])
        print(f"*** {format_roll(roll)} ***")
        print("Enter dice to keep, or (q)uit:")
        keep = input("> ")
        if keep == "q":
            return "q", 0
        # add selected dice to shelf
        shelf = add_to_shelf(keep)
        # score dice on shelf
        turn_points = GameLogic.calculate_score(shelf[0])
        print(f"You have {turn_points} unbanked points and {shelf[1]} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        # return both the user input and the
        return input("> "), turn_points

def start_round(rounds):
    print(f"Starting round {rounds}")

def roll_dice(num):
    return GameLogic.roll_dice(num)

def add_to_shelf(keep):
    return GameLogic.dice_shelf(keep)

def format_roll(roll):
    roll_values = []
    for val in roll:
        roll_values.append(str(val))
    formatted_roll = " ".join(roll_values)
    return formatted_roll

if __name__ == '__main__':
    play()
    # print(GameLogic.calculate_score((1,1,1,1,1)))