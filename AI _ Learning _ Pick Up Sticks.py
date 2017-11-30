"""
2015 Kyle Ulberg
    Contact: kulberg.tech@gmail.com
    I offer this code with no warranty. 
    You, the reader, have full permissions to use, redistribute and edit as you please. 
    Conditions: Credit me as the original author with a link to my source, mention if it was modified, 
        and any redistribution must maintain my disclaimer and its restrictions and must be free. 
        Also, shoot me an email with the appropraite link if you put this anywhere public, as a courtesy. 
    

v1.0    1/29/2015
Initial design.


This code is a self contained learning AI. It is simplified and custom to this game.
Intended as a template for future projects.
"""

import random

# moves_perfect is what we expect moves to match when it finishes learning.
# index is the game state, value is what to take. Value of 3 means bad state, something to avoid.
moves_perfect = [0, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 0]
moves = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
moves_temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Wipes array, then runs n games and prints the resulting "brain" and number of wins.
def auto(n):
    moves_wipe()
    wins = 0
    for i in range(0, n):
        wins += game()
    for i in range(0, 23):
        moves_temp[i] = moves_perfect[i] - moves[i]
    print moves
    print moves_temp
    print wins

# Single game code. Handles game state and initialization.
def game():
    sticks = 22
    temp_wipe()
    # This ensures that the AI always plays second.
    # It was originally intended to play a different learning AI in random order but this was never implemented.
    player = rand_turn
    while True:
        sticks -= player(sticks)
        if player == rand_turn:
            player = AI_learn_turn
        else:
            player = rand_turn
        if sticks < 1:
            if player == AI_learn_turn:
                return 1
            else:
                AI_update()
                return 0
                
# For user play, not implemented.
def player_turn():
    return 0

# Sticks is here for uniform variable player calling
def rand_turn(sticks):
    return random.randint(1, 2)

# On a loss, the most recent unmarked move is marked.
def AI_learn_turn(sticks):
    if moves[sticks] == 0 or moves[sticks] == 3:
        temp = random.randint(1, 2)
        moves_temp[sticks] = temp
        return temp
    else:
        moves_temp[sticks] = moves[sticks]
        return moves[sticks]

# Updates 
def AI_update():
    for i in range(2, 23):
        if moves_temp[i] == 0:
            pass
        elif moves[i] == 3:
            pass
        elif moves[i] == 0:
            moves[i] = 3 - moves_temp[i]
            print "AI Updated. " + str(i) + "    " + str(moves[i])
            return 1
        elif moves[i] == moves_temp[i]:
            moves[i] = 3
            print "AI Updated. Bad state discovered. " + str(i) + "    " + str(moves[i])
            return 2
    return 3

def moves_wipe():
    for i in range(0, 23):
        moves[i] = 0

def temp_wipe():
    for i in range(0, 23):
        moves_temp[i] = 0

