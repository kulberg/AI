import time
import random

#Fucking insane

grid = {}
memory = {}
memory_new = {}
state = [000000000000000000000000000000]

def grid_set():
    grid['AI'] = [0, 'EI', 'AL']
    grid['AL'] = [0, 'AI', 'BL', 'AP']
    grid['AP'] = [0, 'AL', 'DP']
    grid['BJ'] = [0, 'EJ', 'BL']
    grid['BL'] = [0, 'BJ', 'AL', 'CL', 'BO']
    grid['BO'] = [0, 'BL', 'DO']
    grid['CK'] = [0, 'EK', 'CL']
    grid['CL'] = [0, 'CK', 'BL', 'CN']
    grid['CN'] = [0, 'CL', 'DN']
    grid['EI'] = [0, 'AI', 'HI', 'EJ']
    grid['EJ'] = [0, 'EI', 'BJ', 'GJ', 'EK']
    grid['EK'] = [0, 'EJ', 'CK', 'FK']
    grid['DN'] = [0, 'CN', 'FN', 'DO']
    grid['DO'] = [0, 'DN', 'BO', 'GO', 'DP']
    grid['DP'] = [0, 'DO', 'AP', 'HP']
    grid['FK'] = [0, 'EK', 'FM']
    grid['FM'] = [0, 'FK', 'FN', 'GM']
    grid['FN'] = [0, 'FM', 'DN']
    grid['GJ'] = [0, 'EJ', 'GM']
    grid['GM'] = [0, 'GJ', 'FM', 'HM', 'GO']
    grid['GO'] = [0, 'GM', 'DO']
    grid['HI'] = [0, 'EI', 'HM']
    grid['HM'] = [0, 'HI', 'GM', 'HP']
    grid['HP'] = [0, 'HM', 'DP']

def new_memory():
    if memory_new.keys()[0] in memory:
        memory[memory_new.keys()[0]].append(memory_new[memory_new.keys()[0]])
    else:
        if memory_new.keys()[0][0] == 1 or memory_new.keys()[0][0] == 4:
            memory[memory_new.keys()[0]] = memory_new[memory_new.keys()[0]]
        else:
            memory[memory_new.keys()[0]] = [memory_new[memory_new.keys()[0]]]
    print memory_new
    memory_new.clear()

def time_run(n):
    t = time.clock()
    i = len(memory)
    print run(n)
    print str(len(memory) - i) + " New Memories."
    return "Completed " + str(n) + " Operations in " + str(time.clock() - t) + " Seconds."

def run(n):
    wins = 0
    draws = 0
    for i in range(0, n):
        res = game()
        if res == 1:
            wins += 1
        elif res == 0:
            draws += 1
    return wins, draws

#Game and Memory, then beer! 
def game():
    grid_set()
    turns_since_mill = 0
    for i in range(0, 9):
        if not place(1) == 2:
            turns_since_mill += 1
        else:
            turns_since_mill = 0
        moved = place(2)
        if moved == 1:
            turns_since_mill += 1
        elif moved == 2:
            turns_since_mill = 0
        else:
            return 2
    done = False
    player = 1
    while not done:
        if len(grid_search(player)) < 3:
            if player == 2:
                new_memory()
            return player
        elif len(grid_search(player)) == 3:
            if not hop(player) == 2:
                turns_since_mill += 1
            else:
                turns_since_mill = 0
        else:
            moved = move(player)
            if moved == 0:
                if player == 2:
                    new_memory()
                return player
            elif moved == 1:
                turns_since_mill += 1
            else:
                turns_since_mill = 0
        player = 3 - player
        if turns_since_mill == 50:
            return 0

def game_state(turn_type):
    temp = str(turn_type)
    for i in grid.values():
        temp += str(i[0])
    return temp

def grid_print():
    for i in grid:
        if not grid[i][0] == 0:
            print i, grid[i][0]

#0 returns empty spaces.
#1 returns player 1 pieces.
#2 returns player 2 pieces.
def grid_search(player):
    temp = []
    for i in grid:
        if grid[i][0] == player:
            temp.append(i)
    return temp

def place(player):
    valid = valid_place()
    if player == 2:
        state[0] = game_state(1)
        if state[0] in memory:
            mem = memory[state[0]]
        else:
            mem = []
        res = list(set(valid) - set(mem))
        if res == []:
            return 0
        loc = res[random.randint(0, len(res) - 1)]
        memory_new.clear()
        memory_new[state[0]] = loc
    else:
        loc = valid[random.randint(0, len(valid) - 1)]
    grid[loc][0] = player
    if is_mill(loc):
        remove(player)
        return 2
    return 1

def valid_place():
    return grid_search(0)

def move(player):
    valid = valid_move(player)
    res = []
    if player == 2:
        state[0] = game_state(2)
        if state[0] in memory:
            mem = memory[state[0]]
        else:
            mem = []
        for i in valid:
            if not i in mem:
                res.append(i)
    else:
        res = valid
    if res == []:
        return 0
    loc = res[random.randint(0, len(res) - 1)]
    if player == 2:
        memory_new.clear()
        memory_new[state[0]] = loc
    grid[loc[0]][0] = 0
    grid[loc[1]][0] = player
    if is_mill(loc):
        remove(player)
        return 2
    return 1

def valid_move(player):
    temp = []
    player_pieces = grid_search(player)
    empty = grid_search(0)
    for i in player_pieces:
        for j in empty:
            if j in grid[i]:
                temp.append([i, j])
    return temp

def hop(player):
    valid = valid_hop(player)
    if player == 2:
        state[0] = game_state(3)
        if state[0] in memory:
            mem = memory[state[0]]
        else:
            mem = []
        res = []
        for i in valid:
            if not i in mem:
                res.append(i)
        loc = res[random.randint(0, len(res) - 1)]
        memory_new.clear()
        memory_new[state[0]] = loc
    else:
        loc = valid[random.randint(0, len(valid) - 1)]
    grid[loc[0]][0] = 0
    grid[loc[1]][0] = player
    if is_mill(loc):
        remove(player)
        return 2
    return 1

def valid_hop(player):
    temp = []
    player_pieces = grid_search(player)
    empty = grid_search(0)
    for i in player_pieces:
        for j in empty:
            temp.append([i, j])
    return temp

def remove(player):
    valid = valid_remove(player)
    if player == 2:   
        state[0] = game_state(4)
        if state[0] in memory:
            mem = memory[state[0]]
        else:
            mem = []
        res = list(set(valid) - set(mem))
        loc = res[random.randint(0, len(res) - 1)]
        memory_new.clear()
        memory_new[state[0]] = loc
    else:
        loc = valid[random.randint(0, len(valid) - 1)]
    grid[loc][0] = 0
    return 1

def valid_remove(player):
    temp = []
    enemy_pieces = grid_search(3 - player)
    for i in enemy_pieces:
        if not is_mill(i):
            temp.append(i)
    if temp == []:
        return enemy_pieces
    else:
        return temp

def is_mill(loc):
    if type(loc) == list:
        loc = loc[1]
    temp = []
    player = grid[loc][0]
    player_pieces = grid_search(player)
    for i in grid:
        if loc[0] in i:
            temp.append(i)
    if list(set(temp) - set(player_pieces)) == []:
        return True
    temp = []
    for i in grid:
        if loc[1] in i:
            temp.append(i)
    if list(set(temp) - set(player_pieces)) == []:
        return True
    return False

def loss(player):
    if player == 1:
        print "Winner!"
    else:
        print "You Lose."
    return 1

