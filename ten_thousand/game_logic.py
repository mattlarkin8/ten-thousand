import random
from collections import Counter

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))

        return tuple(rolls)

    @staticmethod
    def calculate_score(tup):
        score = 0
        roll = Counter(tup).most_common()

        if len(tup) == 0:
            return score

        print(f"print roll: {roll}")

        # straight
        if len(roll) == 6:
            return 1500

        #6 of a kind
        if roll[0][1] == 6:
            if roll[0][0] == 1:
                score += 4000
                return score
            score += int(roll[0][0]) * 400
            return score

        #5 of a kind
        elif roll[0][1] == 5:
            if roll[0][0] == 1:
                score += 3000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50

                elif roll[1][0] == 1:
                    score += 100

            else:
                score += int(roll[0][0]) * 300
                return score

        #4 of a kind
        elif roll[0][1] == 4:
            if roll[0][0] == 1:
                score += 2000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50 * roll[1][1]

                elif roll[1][0] == 1:
                    score += 100 * roll[1][1]

                elif roll[2][0] == 5:
                    score += 50 * roll[2][1]

                elif roll[2][0] == 1:
                    score += 100 * roll[2][1]

            else:
                score += int(roll[0][0]) * 200
                return score

        # double 3 of a kind
        elif len(roll) == 2:
            if roll[0][1] == 3 and roll[1][1] == 3:
                if roll[0][0] == 1:
                    score += 1000
                    return score + roll[1][0] * 100

                if roll[1][0] == 1:
                    score += 1000
                    return score + roll[0][0] * 100

                return roll[0][0] * 100 + roll[1][0] * 100

        # 3 of a kind
        elif roll[0][1] == 3:
            if roll[0][0] == 1:
                score += 1000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50 * roll[1][1]

                elif roll[1][0] == 1:
                    score += 100 * roll[1][1]

                elif roll[2][0] == 5:
                    score += 50 * roll[2][1]

                elif roll[2][0] == 1:
                    score += 100 * roll[2][1]

                elif roll[3][0] == 5:
                    score += 50 * roll[3][1]

                elif roll[3][0] == 1:
                    score += 100 * roll[3][1]

            else:
                score += int(roll[0][0]) * 100
                return score

        # 3 pairs
        elif len(roll) > 2:
            if roll[0][1] and roll[1][1] and roll[2][1] == 2:
                score += 1500
                return score

        #********Commented out after working with Roger
        # Should a full house exist as a valid score?
        # # full house
        # elif len(roll) >= 2:
        #     if roll[0][1] == 3 and roll[1][1] == 2:
        #         score += 1500
        #
        #     elif len(roll) == 3:
        #         if roll[2][0] == 5:
        #             score += 50
        #
        #         elif roll[2][0] == 1:
        #             score += 100
        #
        #     return score

        # pair 1's
        elif roll[0][1] == 2 and roll[0][0] == 1:
            score += 200

        # pair 5's
        elif roll[0][1] == 2 and roll[0][0] == 5:
            score += 100

        elif len(roll) > 1:
            if roll[1][1] == 2 and roll[1][0] == 5:
                score += 100

        # single 1's
        elif roll[0][0] == 1:
            score += 100

        # single 5's
        elif roll[0][0] == 5:
            score += 50

        return score