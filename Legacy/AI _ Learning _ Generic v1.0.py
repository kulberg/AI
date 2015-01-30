"""
Copyright 2015 Kyle Ulberg
    Contact: kulberg.tech@gmail.com
    I offer this software with no warranty. 
    You, the reader, have full permissions to use, redistribute and edit as you please. 
    Conditions: Credit me as the original author with a link to my source, mention if it was modified, 
        and any redistribution must maintain my copyright and it's restrictions and must be free. 
        Also, shoot me an email with the appropraite link if you put this anywhere public, as a courtesy. 


v1.0    1/29/2015
Developed for scientific, scholastic and proof-of-concept purposes. 
To be used with "AI _ Module.py" and various custom game modules. 


There are many ways to learn, but the simplest and most effective way is to not repeat mistakes. 
This approach is, of course, far from efficient. Also, rather useless in games based primarily on chance. 
However, it can be abstracted to the point at which the AI has absolutely no direct access to information from the game such as the board or what the moves actually are.
This allows much greater potential for modularity. I could, potentially, make a game about the stock market given historical data for state and say loss if <20% profit. 
Or I could make another for backgammon. Chess. 

I could even make a game out of writing learning AI. 

All of these could even use the same code. Below is my first attempt at this. I will expand and revise as necessary. 
"""

import random

class AI:
    # In Python, declaring a variable here means that it is shared with ALL instances of the object AI.
    # Note that last_state and last_move are NOT here. This means that mistakes are tracked independently, but are learned from by every AI at the same time. 
    #     Their temp variables are instanced to avoid conflict and smooth runtime. Keeps things simple in "AI _ Module"
    # Ideal for most cases. 
    memory = {}
    memories = 0
    
    def __init__(self):
        # Contrary to above, declaring memory here instead stores a seperate dictionary named memory for each instance of AI. 
        #     Note that I never use __init__(self) or AI_player.__init__() to wipe these variables. That is in case you choose to do this. 
        #     Use print_intersect(player1, player2) in "AI _ Module" to see where your seperate player memories are equivalent. 
        # Can be useful for finding unusual patterns or if you want to study the various effects of player order. 
        #     Note, however, that the second player will always win my sample game if played perfectly. In this particular case, it is easier to see the pattern with shared memory. 
        # For cases in which a specific player has a different set of moves ("director" or such), make that a different turn type in game_state() rather than making memory local. 
        #     Alternative to doing this, add the player number into game_state(). 
        #self.memory = {}
        self.last_state = ''
        self.last_move = ''
    
    # The grit. This function handles all learning, based upon a few simple rules. 
    # Worth saying explicitly: the values in memory are what NOT to do. -1 denotes "bad state," a game state in which you will lose if the opponent doesn't make a mistake. 
    def new_memory(self):
        # These next few lines check for an alternative "end state" in which ever possible move is a losing move. O(n) with len(memory)
        #     This end state will not crash the program, but can be useful. Usually unneccesary. 
        if len(self.memory) == 0:
            done = False
        else:
            done = True
        for i in self.memory.values():
            if not i == -1:
                done = False
        if done == True:
            return -1
        # End end state check. 
        
        # Begin grit. 
        # Empty last_state and last_move happen often in later iterations, especially in games with few states. 
        #       This is because of the bad state marker (see turn()). Unnecessary, but cleaner and saves RAM. 
        elif self.last_state == '':
            return 0
        # If a record for last_state exists, add to the list...
        elif self.last_state in self.memory:
            self.memory[self.last_state].append(self.last_move)
        # ...otherwise, make a new list. 
        else:
            self.memory[self.last_state] = [self.last_move]
        # Wipe temps every time, just in case. 
        self.last_state = ''
        self.last_move = ''
        self.memories += 1
    
    # Handles individual turns. Note that there is no player variable passed here. 
    #     Since each player is an individual instance of AI, they each get their own copy of this function. If the active player is important in a given game state, put it in game_state(). 
    # state can be 'special,' but this is rarely useful other than a setting a command to trigger upon a win or loss. 
    #     Just add extra elifs for more special states. 
    # valid is len(valid_moves), where valid_moves is a list of possible valid moves. 
    #     Formatting doesn't matter, just get the length right. None of that extra information will be used (or even seen!) here. 
    # state(string) and valid(int) are computed and passed by the game through "AI _ Module"
    # If there are more than one OK'd moves, returns random from among them. 
    def turn(self, state, valid):
        if state == -1:
            #loss
            return self.new_memory()
        elif state == -2:
            #win
            self.last_state = ''
            self.last_move = ''
        elif valid < 1:
            print "AI recieved len(valid_moves()) < 1." 
            return 0
        # Prevents http://xkcd.com/371/
        elif not state in self.memory:
            self.last_state = state
            move = random.randint(0, valid - 1)
            self.last_move = move
            return move
        # If the current state is marked "bad," then the move that put you here is also bad. Prevent that. 
        elif self.memory[state] == -1:
            self.new_memory()
            return random.randint(0, valid - 1)
        # If every valid move at this state leads to a loss, then this is a "bad" state. Mark it as such for future reference. 
        #     This starts out simple enough - The move that actually made you lose quickly gets marked bad. 
        #     But then the above elif sees that and learns not to make moves that put you into this state. 
        #     Eventually, only the perfect moves remain or every move gets marked bad. Either way, you learned something about the game. 
        elif len(self.memory[state]) == valid:
            self.new_memory()
            self.memory[state] = -1
            return random.randint(0, valid - 1)
        # Specific boundings - 
        #     if 0 < len(memory[state]) < valid and not memory[state] == -1: 
        # Return random from 0 -> valid - 1
        #     The idea is that in game, you can simply go valid_moves[valid] 
        else:
            self.last_state = state
            temp = []
            for i in range(0, valid):
                temp.append(i)
            temp = list(set(temp) - set(self.memory[state]))
            move = temp[random.randint(0, len(temp) - 1)]
            self.last_move = move
            return move
    
