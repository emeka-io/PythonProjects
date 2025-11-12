# Python-Projects
## Quick Start


This is a fully functional Tic-Tac-Toe game written in pure Python, that shows how game loops, player turns, and AI logic work.

The game runs directly in the terminal — no external libraries or frameworks needed.

✨ Features

🧩 Two Modes:

Player vs Player

Player vs Computer (AI using simple logic or minimax algorithm)

🧠 AI Mode: Computer analyzes moves and plays optimally.

🧹 Clean Codebase: Fully commented, PEP8-compliant, and easy to follow.

💾 No Dependencies: Runs on standard Python — no pygame or extra installs needed.

📖 Educational: Includes clear docstrings and comments explaining each part of the logic.


🧠 What the program shows

How to structure a small game loop in Python.

How to handle user input and validate moves.

How to implement basic AI and winning logic.

How to write clean, modular, and documented Python code.

🧑‍💻 Author

Your Name (GitHub: @emeka-io)

Built as part of my Python learning journey, learning how to build real programming projects.

Feel free to fork, improve, and share!


```bash
# Run the game:
python tictactoe.py

# Run unit tests:
python tictactoe.py test
```

## Gameplay

**Modes:**
- **Human vs Human**: Two players alternate turns on the same machine.
- **Human vs AI**: You play against an unbeatable AI using the minimax algorithm.

**Board Layout:**
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

Enter the position number (1–9) where you want to place your mark.

**Winning:**
- Get 3 marks in a row (horizontal, vertical, or diagonal) to win.
- The game tracks wins, losses, and draws in `high_scores.json`.

## Features

✅ **Minimax Algorithm**: The AI is unbeatable—it explores all possible game states to find the optimal move.  
✅ **High Score Tracking**: Game results are saved and displayed.  
✅ **Input Validation**: Handles invalid inputs gracefully.  
✅ **Unit Tests**: 8 tests covering board logic, win detection, and AI behavior.  
✅ **Clean Code**: Type hints, docstrings, and clear separation of concerns.

## Design Rationale

The code separates concerns into four main classes:

1. **Board**: Manages game state (grid, moves, win detection).
2. **AI**: Implements minimax—a recursive algorithm that evaluates all possible game continuations.
3. **ScoreManager**: Handles persistence (reading/writing high scores to JSON).
4. **Game**: Orchestrates the game loop, input, and flow.

This modularity makes it easy to test individual components, extend the game (e.g., add difficulty levels), or swap rendering backends.

The **minimax algorithm** works by:
- Recursively exploring all possible moves from the current position.
- Assigning scores to terminal states: AI win = +10, human win = −10, draw = 0.
- The AI (maximizer) chooses moves that maximize the score; the human (minimizer) is assumed to play optimally to minimize.
- Depth is used to prefer quicker wins.

## Example Session

```
========================================
         TIC-TAC-TOE GAME
========================================
  [1] Human vs Human
  [2] Human vs AI (Minimax)
  [3] View High Scores
  [4] Exit
========================================

Choose an option: 2

     BOARD
  ─────────────
  1 | 2 | 3
  ─────────────
  4 | 5 | 6
  ─────────────
  7 | 8 | 9
  ─────────────

Player X, enter position (1-9): 5

     BOARD
  ─────────────
  1 | 2 | 3
  ─────────────
  4 | X | 6
  ─────────────
  7 | 8 | 9
  ─────────────

  🤖 AI plays position 1.

     BOARD
  ─────────────
  O | 2 | 3
  ─────────────
  4 | X | 6
  ─────────────
  7 | 8 | 9
  ─────────────

Player X, enter position (1-9): 9

     BOARD
  ─────────────
  O | 2 | 3
  ─────────────
  4 | X | 6
  ─────────────
  7 | 8 | X
  ─────────────

  🤖 AI plays position 5.
(AI blocks or continues—never loses!)
```

## Testing

Run the test suite to verify core logic:

```bash
python tictactoe.py test
```

Tests cover:
- Board initialization and move validity
- Win detection (rows, columns, diagonals)
- Draw detection
- AI's ability to find winning moves
- AI's ability to block human wins

---

**Total Lines**: ~650 (well under 1200 limit)  
**Dependencies**: None (pure Python 3.10+)  
**Last Updated**: November, 12 2025 (BY EMEKA)

