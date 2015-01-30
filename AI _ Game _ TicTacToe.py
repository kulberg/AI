"""
Copyright 2015 Kyle Ulberg
    Contact: kulberg.tech@gmail.com
    I offer this software with no warranty. 
    You, the reader, have full permissions to use, redistribute and edit as you please. 
    Conditions: Credit me as the original author with a link to my source, mention if it was modified, 
        and any redistribution must maintain my copyright and it's restrictions and must be free. 
        Also, shoot me an email with the appropraite link if you put this anywhere public, as a courtesy. 


v1.0    1/30/2015
Developed as an example for "AI _ Learning _ Generic.py" and "AI _ Module.py"
To be used alongside both. 

Classic Tic-Tac-Toe.
Total memories until permanent draws: Variable, 2-3k. Most game states will never be reached. I will try making a more 'human' representation to see if I can improve this. 
Games required: Variable, 4-6k. 
Time: 10-15s on my laptop. 1 million games: 3 minutes
Analysis: AI1.memory doesn't fit in my terminal. I will need to write a function for this. 


# Total runs - draws.
1000000 - run(1000000)
Out[7]: 5165

# Total memories recorded.
AI1.memories
Out[8]: 2632

# Total game states in memory.
len(AI1.memory)
Out[9]: 2485


Comments later. 
"""


import math
import random

class game_tictactoe:
    
    record = [['000000000', 0]]
    
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.track = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player = random.randint(1, 2)
        # self.piece makes sure that I always start with the same variable. 
        # This would halve my game states if I were storing end states in memory, since half of the end states are only possible if player 'O' goes first - odd number grid. 
        # So basically, for posterity. 
        self.piece = 'X'
        
    def game_state(self):
        res = ''
        for i in self.board:
            res += str(i)
        return res

    def valid_moves(self):
        res = []
        for i in range(0, 9):
            if self.board[i] == 0:
                res.append(i)
        return res
    
    # Call with (-)winning player, draw (-3), or move
    # self.record[i] = [n, x]
    #     n is a step-through of the game. ie, first move is 3, second 5  =>  '000102000'
    #     x = winning player or 3 for draw
    def tracker(self, x):
        # After a move, num = move number, 1 -> 9 
        num = 9 - len(self.valid_moves())
        #draw
        if x < 0:
            res = ''
            for i in self.track:
                res += str(i)
            self.record.append([res, -x])
            self.track = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self.track[x] = num
    
    # returns the losing player
    def turn(self, move):
        self.board[move] = self.piece
        self.tracker(move)
        row = int(math.floor(move/3))
        column = move % 3
        if self.board[3 * row] == self.piece and self.board[3 * row + 1] == self.piece and self.board[3 * row + 2] == self.piece:
            self.tracker(-self.player)
            return 3 - self.player
        elif self.board[column] == self.piece and self.board[3 + column] == self.piece and self.board[6 + column] == self.piece:
            self.tracker(-self.player)
            return 3 - self.player
        elif len(self.valid_moves()) == 0:
            self.tracker(-3)
            return -1
        else:
            self.player = 3 - self.player
            if self.piece == 'X':
                self.piece = 'O'
            else:
                self.piece = 'X'
            return 0