# Rock paper scissors
import random, sys

print("ROCK, PAPER, SCISSORS")

# These variables keep track of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:  # The main game loop
    print("%s wins, %s losses, %s ties" % (wins, losses, ties))
    while True:  # Player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type r, p, s, or q")

    # Display player choice:
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

    # Display computer choice:
    computerMove = ""
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    if randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    if randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    # Display and record scores
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses = losses + 1
