# Tic-Tac-Toe AI

## Project Overview
This project is a terminal-based Tic-Tac-Toe game where a human plays against an unbeatable AI. The AI uses the Minimax algorithm with alpha-beta pruning to evaluate every possible move and choose the optimal response.

## Features
- Human plays as X and AI plays as O
- Clean 3x3 board display
- Input validation for numeric, range, and occupied-cell errors
- Unbeatable AI using recursive Minimax logic
- Game-over announcements for win or draw
- Replay option after each game

## Folder Structure
```text
tic_tac_toe_ai/
├── main.py
├── game.py
├── ai.py
├── utils.py
├── README.md
└── requirements.txt
```

## Installation
1. Open a terminal in this project folder.
2. Run:
   ```bash
   python -m pip install -r requirements.txt
   ```

## How to Run
```bash
python -m tic_tac_toe_ai.main
```

## How the Minimax Algorithm Works
Minimax evaluates the board recursively by assuming the human will play optimally and the AI will play optimally. Each move is scored as:
- `+10` for a winning move
- `-10` for a losing move
- `0` for a draw

The AI explores all possible future moves and picks the move that maximizes its chances of winning while minimizing the human's chances.

## Example Gameplay
```text
Welcome to Tic-Tac-Toe AI!
You are X and the AI is O.
Choose a cell from 1 to 9.

 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 

Choose a position from 1 to 9: 5
AI plays at position 1.
```
