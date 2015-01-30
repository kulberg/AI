"""
Copyright 2015 Kyle Ulberg
    Contact: kulberg.tech@gmail.com
    I offer this software with no warranty. 
    You, the reader, have full permissions to use, redistribute and edit as you please. 
    Conditions: Credit me as the original author with a link to my source, mention if it was modified, 
        and any redistribution must maintain my copyright and it's restrictions and must be free. 
        Also, shoot me an email with the appropraite link if you put this anywhere public, as a courtesy. 
    

v1.0    1/29/2015
Developed as a bridge between "AI _ Learning _ Generic.py" and a variety of custom game modules.  


Serves to communicate between the above mentioned modules. 
"""

# Import modules
# In future versions, game will be variable. 
import time
AI_class = __import__("AI _ Learning _ Generic").AI
#Game_class = __import__("AI _ Game _ 22 Sticks").game_22sticks
Game_class = __import__("AI _ Game _ TicTacToe").game_tictactoe

# instantiate objects
# In future versions, instantiation will be strictly dynamic. 
game = Game_class()
AI1 = AI_class()
AI2 = AI_class()

# Legacy. Modify per your needs. ie, change temp.append(i) to temp.append(i[1:]) to drop the first char. 
#     Easier to read if you added extra info to game_state() that your AI needs but that you don't want to read. 
# p is player number ONLY. ie, p = 2  ->  print AI2.memory 
def print_memory(p):
    player = eval('AI' + str(game.p))
    temp = []
    for i in player.memory:
        temp.append(i)
    temp.sort()
    for i in temp:
        print i, player.memory[i]

# Useful if you localized memory. Otherwise, pointless. 
def print_intersect(p1, p2):
    player1 = eval('AI' + str(p1))
    player2 = eval('AI' + str(p2))
    res = {}
    for i in player1.memory:
        if i in player2.memory:
            if player1.memory[i] == player2.memory[i]:
                res[i] = player1.memory[i]
    return res

# The driving force. Primary communicator between AI and game. 
# n = number of games
def run(n):
    draws = 0
    i = 0
    while i < n:
        # Keeping a player variable in game lets you compress this function considerably. 
        # Putting active player in game_state() could also be used for this. 
        player = eval('AI' + str(game.player))
        # This tempy saves one really expensive function call. 
        moves = game.valid_moves()
        """
        So this next line is insane. A step-by-step:
            The variables -
                moves is a list of possible moves, so len(moves) is the total number of legal moves for the active player. 
                game.game_state() yields the game state. 
            player.turn(state, valid) returns random (- previous mistakes) from 0 -> valid. Let's call that x...
            ...so, moves[x] gives the chosen move from those valid...
            ...which is passed into game.turn(moves[x]), returning 0 unless the move resulted in a player losing. 
        """
        # My sample game is set to return the losing player. 
        # Otherwise, -1 for special case (draw, etc.), else 0 (continue game) 
        res = game.turn(moves[player.turn(game.game_state(), len(moves))])
        if res == -1:
            reset()
            i += 1
            draws += 1
        elif not res == 0:
            # player.turn(0, 0) can ONLY return -1 for the special end case mentioned in new_memory() in "AI _ Learning _ Generic"
            # I do this instead of directly calling AI_player.new_memory() for easier modification of the losing case. 
            player = eval('AI' + str(res))
            if player.turn(0, 0) == -1:
                return i, draws
            reset()
            i += 1
    return draws

def reset():
    game.__init__()
    # Wipe temps when a game ends. 
    # In future versions, this will be dynamic. 
    AI1.last_state = ''
    AI1.last_move = ''
    AI2.last_state = ''
    AI2.last_move = ''
