# AI
Various experiments with Artificial Intelligence. 

____________________
I have been asked why I didn't teach my earlier learning AI how to play the various games I gave them. \n
That is not learning. That is memory. 
Furthermore, my AI can be used to study things that I cannot calculate by the very nature of my unfortunately limited human mind. 

____________________
Most AI will PREDICT several moves in advance and CALCULATE the VALUE of each game state. 
This is a very limited approach. Prediction can only go so far, since RAM usage grows exponentially with depth. 
Calculating the value so ridiculously often is horrifically slow. And, to top it off, a human had to tell the computer how to rate the value. 
Impressive, but pathetic. 

I want to take Artificial Intelligence to the next level. I want to create an AI that will LEARN for itself... without human influence. 
Untarnished by human limitations. 
I cannot fathom what we could learn from such a creation. And I guess that's the point.

There are many ways to learn, but the simplest and most effective way is to not repeat mistakes. 
This approach is, of course, far from efficient and requires billions of cycles before it can be utilized. (It is easy to visualize as a depth-first search that starts over the first few times it hits a given point on the bottom.)
Let's take Tic-Tac-Toe. There is 1 starting game state, then 9, then 9 * 8, then 9 * 8 * 7, etc. 
So, 2 * 9! (725,760) ending game states since player order matters (odd-number grid). We can chop half, however, with clever code. So 9! is our final answer. 
But we need every playable state, which is 623,530. We need to go through 9 of those to reach an end state. And we can reliably learn only one thing per loss. 
[[UNFINISHED]]

____________________
Anyway...
There are many ways to learn, but the simplest and most effective way is to not repeat mistakes. 
This approach is, of course, far from efficient. Also, rather useless in games based primarily on chance. 
However, it can be abstracted to the point at which the AI has absolutely no direct access to information from the game such as the board or what the moves actually are.
This allows much greater potential for modularity. I could, potentially, make a game about the stock market giving historical data for state and say loss if <20% profit. 
Or I could make another for backgammon. Chess. 

I could even make a game out of writing learning AI. 
