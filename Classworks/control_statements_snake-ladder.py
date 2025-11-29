import random

p1 = input("Enter the p1 Name:")
p2 = input("Enter the p2 Name:")
winning_point = 100
pl_score = 0
p2_score = 0
snakes = {12:6, 21:9, 40:15, 61:22, 99:2}
ladder = {8:16, 23:44, 38:63, 70:88, 89:93}

while pl_score < winning_point and p2_score < winning_point:
    # --- Player 1 Turn ---
    p1_status = input(f"{p1}, want to continue the game (y/n): ")
    if p1_status.lower() == 'y':
        p1_dice = random.randint(1,6)
        print(f"{p1}: Your dice score: {p1_dice}")
        pl_score += p1_dice

        if pl_score in snakes:
            pl_score = snakes[pl_score]
            print(f"Oops! {p1} bitten by snake, go back to {pl_score}")
        elif pl_score in ladder:
            pl_score = ladder[pl_score]
            print(f"Yay! {p1} climbed the ladder, go to {pl_score}")
        else:
            print(f"{p1}: Your total score: {pl_score}")

        if pl_score >= winning_point:
            print(f"Congratulations!!!\n{p1} You won the game")
            break
    else:
        print(f"Congratulations!!!\n{p2} You won the game by forfeit")
        break

    # --- Player 2 Turn ---
    p2_status = input(f"{p2}, want to continue the game (y/n): ")
    if p2_status.lower() == 'y':
        p2_dice = random.randint(1,6)
        print(f"{p2}: Your dice score: {p2_dice}")
        p2_score += p2_dice

        if p2_score in snakes:
            p2_score = snakes[p2_score]
            print(f"Oops! {p2} bitten by snake, go back to {p2_score}")
        elif p2_score in ladder:
            # Corrected typo 'f2_score' to 'p2_score'
            p2_score = ladder[p2_score]
            print(f"Yay! {p2} climbed the ladder, go to {p2_score}")
        else:
            # Added missing else condition for P2
            print(f"{p2}: Your total score: {p2_score}")

        if p2_score >= winning_point:
            print(f"Congratulations!!!\n{p2} You won the game")
            break
    else:
        print(f"Congratulations!!!\n{p1} You won the game by forfeit")
        break
