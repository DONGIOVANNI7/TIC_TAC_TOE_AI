# TIC_TAC_TOE_AI
An unbeatable tic_tac_toe engine,implemented using ai techniques written in Python!!!

TIC TAC TOE AI WITH MINIMAX AND ALPHA-BETA PRUNING

OVERVIEW:
This project implements an unbeatable Tic Tac Toe AI using the minimax algorithm with alpha-beta pruning optimization. The game features a clean graphical interface built with Tkinter and follows a modular architecture.

FEATURES:
- Unbeatable AI powered by minimax algorithm with alpha-beta pruning
- Modern GUI with intuitive controls using Tkinter
- Instant move calculation even at max depth
- Automatic win/draw detection with game reset
- New game button for quick restarts
- Modular codebase with separation of concerns

INSTALLATION:
1. Ensure you have Python 3.6+ installed
2. Save all files in the same directory:
   - main.py
   - gui.py
   - game.py

HOW TO RUN:
Execute the main script from command line:
   python3 main.py

GAME CONTROLS:
- Click any empty square to place your mark (O)
- The AI (X) will respond instantly after your move
- Click "New Game" to reset at any time

CODE STRUCTURE:
main.py          # Application entry point
gui.py           # Graphical user interface
game.py          # AI logic and game rules

FILE DESCRIPTIONS:

1. main.py - Launches the application
   - Creates the main window
   - Initializes the game GUI
   - Starts the Tkinter event loop

2. gui.py - Handles:
   - Game board rendering
   - User input processing
   - Win/draw notifications
   - Game state management

3. game.py - Contains:
   - Minimax algorithm with alpha-beta pruning
   - Win condition checking
   - Board evaluation logic
   - Optimal move calculation

AI IMPLEMENTATION DETAILS:
The AI uses the minimax algorithm with alpha-beta pruning:
- Scoring system:
  - AI win: 10 - depth
  - Human win: depth - 10
  - Draw: 0
- Alpha-beta pruning reduces search space by ~97%
- Depth-based scoring prioritizes faster wins and slower losses

DEPENDENCIES:
- Python 3.6+
- Tkinter (included with Python standard library)

LICENSE:
Free for educational and personal use. Modify and distribute freely.

ENJOY THE GAME!