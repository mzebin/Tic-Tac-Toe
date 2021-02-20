# Tic-Tac-Toe
Tic-Tac-Toe using python3.

## About the Game
The game can be played with computer or with
a friend. The Single Player game has three levels.

### Single Player
  1. Easy
  2. Medium
  3. Impossible

#### Easy
The Easy level chooses the move randomly 
from the available moves.

#### Medium
The computer follows these steps while choosing the move:
  1. Check for a move that can make the computer win. Move there.
  2. Check for a move that will make the player win. if there is,
     block it.
  3. Get the available corner moves, move to a random one.
  4. If the center is free. move there.
  5. Move to a random side space.

#### Impossible
It uses the minimax algorithm to get the best move.
