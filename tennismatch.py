# tennis.py
# This program simulates tennis games
#JULIANA MERCHANT

import random

#A. 6 games < 3 sets < 1 match
games = 1
sets = games*6
match = sets*3

def printIntro():
    # Prints an introduction to the program
    print("This program simulates a game of tennis between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Serve")
    print("alternates every set, but remains throughout one game.\n")
    #match = 3 sets, to win one is 6 games.

def getInputs():
    # Returns probA, proB, number of games to simulate
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of tennis between players a and B
    # Returns number of wins for A, number of wins for B
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def gameOver(a, b):
    # True if game is over, false otherwise
    # 15 love, first match
    if a == 15 or b == 15:
        return a == 15 or b == 15
    # 30, second match
    if a == 30 or b == 30:
        return a == 30 or b == 30
    # 40, third match and end game point
    if a == 40 or b == 40:
        return a == 40 or b == 40
#D. at 40, next point wins set
    if a or b == 41:
        return("We have a winner!")
    # Won all matches.

#F. serving
def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA: # A wins the point
                scoreA = scoreA + 1
            else:                # A loses the point
                serving = "A"
        else:
            if random.random() < probB: # B wins the point
                scoreB = scoreB + 1
            else:                # B loses the point
                serving = "A"
    return scoreA, scoreB

#C. If the games are tied at 6 in a set, a tie breaker is played.
def simTieBreaker(probA, probB):
    serving = "A"
    scoreA = 6
    scoreB = 6
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 2
        else:
            winsB = winsB + 2
    return winsA, winsB


#E. in the event of a deuce (40), the player who makes two points in a row wins.
def simDeuce(pointsDeuce1, pointsDeuce2):
    serving = "A"
    pointsTie1 = 40
    pointsTie2 = 40
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA: # A wins the point
                scoreA = scoreA + 2
            else:                # A loses the point
                serving = "A"
        else:
            if random.random() < probB: # B wins the point
                scoreB = scoreB + 2
            else:                # B loses the point
                serving = "A"
    return scoreA, scoreB

#B. To win the set, the difference must be at least 2 games. If a set is 6-5, then the first
#player needs one more set to win while the second player would need two.
def winSet():
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if winsA == 6:
                random.random() < probA # A wins the point
                scoreA = scoreA + 1
            else:                # A loses the point
                serving = "A"
        else:
            if winsA == 6:
                random.random() < probB # B wins the point
                scoreB = scoreB + 1
            else:                # B loses the point
                serving = "A"
    return scoreA, scoreB

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: " + str(winsA) + " (" + str(winsA / n * 100 ) + "%)")
    print("Wins for B: " + str(winsB) + " (" + str(winsB / n * 100 ) + "%)")

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()


# Use of the 'simOneGame' code lines to attempt the 'deuce','tiebreaker' attribute to error.
# Causes output to stop outputting correct percentages/wins.
# New output gives 'player 1' or, 'player A' the win no matter what, when running.
# 'Game over' may actually be the issue, as well as extremely possible syntax errors 
# One of the changed up 'simOneGame's, according to IDLE.
# The program currently runs (incorrectly) with 0 callback errors.
# Player A will win, and the game will end.


