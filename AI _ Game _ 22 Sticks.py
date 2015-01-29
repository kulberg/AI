"""
Copyright 2015 Kyle Ulberg
    Contact: kulberg.tech@gmail.com
    I offer this software with no warranty. 
    You, the reader, have full permissions to use, redistribute and edit as you please. 
    Conditions: Credit me as the original author with a link to my source, mention if it was modified, 
        and any redistribution must maintain my copyright and it's restrictions and must be free. 
        Also, shoot me an email with the appropraite link if you put this anywhere public, as a courtesy. 


v1.0    1/29/2015
Developed as an example for "AI _ Learning _ Generic.py" and "AI _ Module.py"
To be used alongside both. 

A simple game. Start with 22 sticks and 2 players. 
Each player takes turns taking either 1 or 2 sticks. The player to take the last stick loses.
Note that, if played perfectly, the second player will always win. 
Also note that this game CAN be played perfectly. That's why I picked it. 
"""

import random

class game_22sticks:
    def __init__(self):
        self.sticks = 22
        # Change this to more easily study the effects of player order, but it's not necessary. 
        # Helps with debugging to just set it to 1. 
        self.player = random.randint(1, 2)
    
    # Total states = 44. 1 -> 22 sticks, 2 players. I don't distinguish between players, so I only care about 22. 
    # Can be pretty difficult to write in more complex games, though anything with boards tends to be simpler. Print the board visually for practice. 
    """
    VERY IMPORTANT -- Make damn sure this function's return is consistent. In a given state, it must ALWAYS return the same string. 
    """
    def game_state(self):
        return str(self.sticks)
    
    # The one very difficult function in game. Be sure to keep track of the type of turn. Examples to come. 
    # Should return every possible move for the active player in the given game state. 
    # All of the related computation should ideally be done before returning. 
    # i.e., king with one valid move and bishop with two in chess with no other legal moves could be - 
    #     [['E4', 'E3'], ['A2', 'C4'], ['A2', 'D5']]
    #     In this example, AI_player.turn(state, 3) would be called in "AI _ Module"
    # Complex or otherwise strange moves that don't fit the same format as the rest are fine, such as "Castling" in chess. 
    """
    VERY IMPORTANT -- Make damn sure this function's return is consistent. In a given state, it must ALWAYS return the same list, in the same order. 
        This is why I put things like turn_type in game_state(). Examples to come. 
    """
    def valid_moves(self):
        return [1, 2]
    
    # move = valid_moves()[player.turn(game.game_state(), len(valid_moves()))]
    # move should describe your entire move. ie, (for a rook in chess) B2 to B5  =>  ['B2', 'B5']
    # Note that a queen could also make that move, but 'rook' isn't in the list describing the move.
    #     This is because only one piece can be in that position, so starting_pos can always be used to get the piece type later if necessary...
    #     ...which should NOT be necessary, which is why valid_moves() can be such a pain. 
    def turn(self, move):
        self.sticks -= move
        if self.sticks < 1:
            return 1
        else:
            self.player = 3 - self.player
            return 0
    
