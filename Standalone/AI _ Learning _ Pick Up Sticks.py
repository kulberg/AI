import random

moves_perfect = [0, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 0]
moves = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
moves_temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

def game():
    sticks = 22
    temp_wipe()
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
                print "Updating AI....."
                AI_update()
                return 0

def player_turn():
    #For user play
    return 0

def rand_turn(sticks):
    #Obvious, right?
    return random.randint(1, 2)

def AI_learn_turn(sticks):
    #Always plays second. 
    #The fun bit. Self-updating array. 
    #On a loss, the most recent unmarked move is marked.  
    
    if moves[sticks] == 0 or moves[sticks] == 3:
        temp = random.randint(1, 2)
        moves_temp[sticks] = temp
        return temp
    else:
        moves_temp[sticks] = moves[sticks]
        return moves[sticks]

def AI_update():
    for i in range(2, 23):
        if moves_temp[i] == 0:
            temp = 0
        elif moves[i] == 3:
            temp = 0
        elif moves[i] == 0:
            moves[i] = 3 - moves_temp[i]
            print "AI Updated. " + str(i) + "    " + str(moves[i])
            return 1
        elif moves[i] == moves_temp[i]:
            moves[i] = 3
            print "AI ERROR. Voiding Array. " + str(i) + "    " + str(moves[i])
            return 2
    return 3

def moves_wipe():
    for i in range(0, 23):
        moves[i] = 0

def temp_wipe():
    for i in range(0, 23):
        moves_temp[i] = 0

