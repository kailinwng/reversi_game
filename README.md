# Reversi (Othello) Game in Python

## Overview
This Python program implements a two-player version of the Reversi (Othello) game. Reversi is a classic board game where players take turns placing pieces ('X' and 'O') on a board, flipping opponent's pieces to their own color. The winner is determined based on who has more pieces on the board when no more moves can be made.

## Features
### Board Setup: 
Initializes an 8x8 board with starting pieces in the center.
### Turn-based Gameplay: 
Players take turns making moves, flipping opponent pieces as per the game rules.
### Move Validation: 
Ensures moves are valid based on board boundaries and game rules.
### End Game Detection: 
Automatically detects when the game is over and determines the winner.
### Text-based Interface: 
Uses console output for displaying the game board and taking player inputs.

## Requirements
Python 3.5

## How to Run
1. Ensure you have Python installed on your system.
2. Download or clone the Python Reversi program files from [https://github.com/kailinwng/reversi_game/].
3. Open a terminal or command prompt.
4. Navigate to the directory where the program files are located.
5. Run the following command to start the game:
`python reversi.py`
6. Follow the on-screen instructions to play the game.
7. Enter your move as row col, where row and col are the coordinates of your move on the board.

## Gameplay Instructions
- Players take turns entering their moves by specifying the row and column of the board where they want to place their piece.
- Pieces are placed and opponent pieces are flipped according to Reversi rules.
- The game continues until no more valid moves can be made by either player.
- The player with the most pieces of their color on the board wins. If both players have the same number of pieces, the game ends in a tie.

## Example
$ python reversi.py
  1 2 3 4 5 6 7 8
 +-----------------+
1|   X O          
2|   O X          
3|                
4|                
5|                
6|                
7|                
8|                
 +-----------------+
Current player: X
Enter your move (row col): 3 4
  1 2 3 4 5 6 7 8
 +-----------------+
1|   X O          
2|   O X          
3|       X        
4|                
5|                
6|                
7|                
8|                
 +-----------------+
Current player: O
Enter your move (row col): 
...

## Credits
Developed by Kai Lin Wong [https://www.linkedin.com/in/kai-lin-wong31/]
Inspired by the classic Reversi (Othello) board game.

## Contact
For any questions or feedback, please contact [kailinwng31@gmail.com].
