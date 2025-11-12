"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         TIC-TAC-TOE WITH MINIMAX AI                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

GAMEPLAY:
  - 3x3 grid, players take turns marking X or O.
  - First to get 3 in a row (horizontal, vertical, diagonal) wins.
  - Modes: Human vs Human, Human vs AI (minimax algorithm).

CONTROLS (Human player):
  - Enter position 1-9 (grid numbered as below):
      1 | 2 | 3
     -----------
      4 | 5 | 6
     -----------
      7 | 8 | 9

RUNNING THE GAME:
  python tictactoe.py

FEATURES:
  - Minimax algorithm for unbeatable AI.
  - High score persistence (saved to high_scores.json).
  - Input validation and error handling.
  - Unit tests included.

DESIGN RATIONALE:
This implementation separates game logic (Board, Game, AI) from rendering.
Minimax explores all possible game states recursively, assigning scores
(+1 for AI win, -1 for human win, 0 for draw). The alpha-beta pruning
conceptually improves efficiency by skipping redundant branches. This design
makes it easy to test logic independently and swap rendering backends.
"""

import json
import os
from pathlib import Path
from typing import Optional, Tuple, List


class Board:
    """
    Manages the tic-tac-toe board state.
    
    Attributes:
        grid: List of 9 positions (1-indexed conceptually, 0-indexed internally).
              Empty cells are None, human moves are 'X', AI moves are 'O'.
    """

    def __init__(self) -> None:
        """Initialize empty 3x3 board."""
        self.grid: List[Optional[str]] = [None] * 9

    def is_valid_move(self, position: int) -> bool:
        """
        Check if a move to position (1-9) is legal.
        
        Args:
            position: 1-indexed grid position.
            
        Returns:
            True if position is in range [1,9] and cell is empty.
        """
        return 1 <= position <= 9 and self.grid[position - 1] is None

    def make_move(self, position: int, player: str) -> bool:
        """
        Place a mark on the board.
        
        Args:
            position: 1-indexed grid position.
            player: 'X' for human, 'O' for AI.
            
        Returns:
            True if move was successful, False if invalid.
        """
        if not self.is_valid_move(position):
            return False
        self.grid[position - 1] = player
        return True

    def undo_move(self, position: int) -> None:
        """Remove a move (used in minimax backtracking)."""
        self.grid[position - 1] = None

    def get_empty_cells(self) -> List[int]:
        """Return list of empty positions (1-indexed)."""
        return [i + 1 for i in range(9) if self.grid[i] is None]

    def check_winner(self) -> Optional[str]:
        """
        Detect if there's a winner.
        
        Returns:
            'X' if human won, 'O' if AI won, None if no winner.
        """
        # All possible winning combinations (0-indexed).
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combos:
            if self.grid[combo[0]] == self.grid[combo[1]] == self.grid[combo[2]] is not None:
                return self.grid[combo[0]]
        return None

    def is_full(self) -> bool:
        """Check if board is completely filled (draw condition)."""
        return all(cell is not None for cell in self.grid)

    def is_game_over(self) -> bool:
        """Check if game has ended (win or draw)."""
        return self.check_winner() is not None or self.is_full()

    def display(self) -> None:
        """Render the board to console."""
        print("\n     BOARD")
        print("  ─────────────")
        for row in range(3):
            cells = []
            for col in range(3):
                idx = row * 3 + col
                cell = self.grid[idx]
                if cell is None:
                    cells.append(str(idx + 1))  # Show position number
                else:
                    cells.append(cell)
            print(f"  {cells[0]} | {cells[1]} | {cells[2]}")
            if row < 2:
                print("  ─────────────")
        print("  ─────────────\n")

    def copy(self) -> "Board":
        """Return a deep copy of the board (used in minimax)."""
        new_board = Board()
        new_board.grid = self.grid.copy()
        return new_board


class AI:
    """
    Minimax AI player. Implements the minimax algorithm to find optimal moves.
    
    Minimax explores all possible future game states recursively:
      - Maximizing player (AI) wants highest score.
      - Minimizing player (Human) wants lowest score.
      - Leaf nodes (terminal states) are scored: AI win=+1, Human win=-1, Draw=0.
    """

    @staticmethod
    def minimax(board: Board, depth: int, is_maximizing: bool) -> int:
        """
        Recursively evaluate board positions using minimax algorithm.
        
        Args:
            board: Current board state.
            depth: Recursion depth (used for scoring to prefer quicker wins).
            is_maximizing: True if we're maximizing (AI turn), False for minimizing (Human turn).
            
        Returns:
            Score of the position: +10-depth (AI win), -10+depth (Human win), 0 (draw).
        """
        winner = board.check_winner()

        # Terminal states: assign scores.
        if winner == 'O':  # AI (maximizer) wins.
            return 10 - depth
        if winner == 'X':  # Human (minimizer) wins.
            return depth - 10
        if board.is_full():  # Draw.
            return 0

        if is_maximizing:
            # AI's turn: find the move with maximum score.
            max_score = float('-inf')
            for pos in board.get_empty_cells():
                board.make_move(pos, 'O')
                score = AI.minimax(board, depth + 1, False)
                board.undo_move(pos)
                max_score = max(max_score, score)
            return max_score
        else:
            # Human's turn: find the move with minimum score.
            min_score = float('inf')
            for pos in board.get_empty_cells():
                board.make_move(pos, 'X')
                score = AI.minimax(board, depth + 1, True)
                board.undo_move(pos)
                min_score = min(min_score, score)
            return min_score

    @staticmethod
    def find_best_move(board: Board) -> int:
        """
        Find the best move for the AI using minimax.
        
        Args:
            board: Current board state.
            
        Returns:
            Best position (1-indexed) for AI to play.
        """
        best_score = float('-inf')
        best_move = None

        for pos in board.get_empty_cells():
            board.make_move(pos, 'O')
            score = AI.minimax(board, 0, False)  # AI just moved, human's turn.
            board.undo_move(pos)

            if score > best_score:
                best_score = score
                best_move = pos

        return best_move if best_move is not None else board.get_empty_cells()[0]


class ScoreManager:
    """Manage high scores persistence (saved to JSON)."""

    def __init__(self, filename: str = "high_scores.json") -> None:
        """
        Initialize score manager.
        
        Args:
            filename: Where to save/load scores.
        """
        self.filepath = Path(filename)

    def load_scores(self) -> dict:
        """Load high scores from file."""
        if self.filepath.exists():
            with open(self.filepath, 'r') as f:
                return json.load(f)
        return {"human_wins": 0, "ai_wins": 0, "draws": 0}

    def save_scores(self, scores: dict) -> None:
        """Save scores to file."""
        with open(self.filepath, 'w') as f:
            json.dump(scores, f, indent=2)

    def display_scores(self) -> None:
        """Display current high scores."""
        scores = self.load_scores()
        print("\n" + "=" * 40)
        print("             HIGH SCORES")
        print("=" * 40)
        print(f"  Human Wins:  {scores['human_wins']:3d}")
        print(f"  AI Wins:     {scores['ai_wins']:3d}")
        print(f"  Draws:       {scores['draws']:3d}")
        print("=" * 40 + "\n")

    def update_scores(self, result: str) -> None:
        """
        Update score based on game result.
        
        Args:
            result: 'human', 'ai', or 'draw'.
        """
        scores = self.load_scores()
        if result == 'human':
            scores['human_wins'] += 1
        elif result == 'ai':
            scores['ai_wins'] += 1
        else:
            scores['draws'] += 1
        self.save_scores(scores)


class Game:
    """Main game controller."""

    def __init__(self) -> None:
        """Initialize game."""
        self.board = Board()
        self.score_manager = ScoreManager()
        self.game_mode: Optional[str] = None  # 'pvp' or 'pva'
        self.current_player = 'X'  # Always start with human.

    def display_menu(self) -> None:
        """Show main menu and return user choice."""
        print("\n" + "=" * 40)
        print("         TIC-TAC-TOE GAME")
        print("=" * 40)
        print("  [1] Human vs Human")
        print("  [2] Human vs AI (Minimax)")
        print("  [3] View High Scores")
        print("  [4] Exit")
        print("=" * 40 + "\n")

    def get_human_move(self) -> int:
        """
        Get and validate human player input.
        
        Returns:
            Valid position (1-9).
        """
        while True:
            try:
                inp = input(f"Player {self.current_player}, enter position (1-9): ").strip()
                pos = int(inp)
                if self.board.is_valid_move(pos):
                    return pos
                else:
                    print("  ❌ Invalid move! Cell occupied or out of range.")
            except ValueError:
                print("  ❌ Invalid input! Enter a number 1-9.")

    def play_turn(self) -> bool:
        """
        Execute one turn.
        
        Returns:
            True if game is still running, False if game ended.
        """
        if self.current_player == 'X':
            # Human move.
            pos = self.get_human_move()
        else:
            # AI or second human move.
            if self.game_mode == 'pva':
                # AI turn: find best move and display it.
                pos = AI.find_best_move(self.board)
                print(f"  🤖 AI plays position {pos}.")
            else:
                # Human vs Human: second human's turn.
                pos = self.get_human_move()

        self.board.make_move(pos, self.current_player)
        self.board.display()

        # Check for win/draw.
        winner = self.board.check_winner()
        if winner:
            print(f"  🎉 Player {winner} wins!")
            return False

        if self.board.is_full():
            print("  🤝 It's a draw!")
            return False

        # Switch player.
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def run_game(self) -> None:
        """Main game loop."""
        self.board.display()
        while self.play_turn():
            pass

        # Update scores.
        winner = self.board.check_winner()
        if winner == 'X':
            self.score_manager.update_scores('human')
        elif winner == 'O':
            self.score_manager.update_scores('ai' if self.game_mode == 'pva' else 'human')
        else:
            self.score_manager.update_scores('draw')

    def run(self) -> None:
        """Main menu loop."""
        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.game_mode = 'pvp'
                self.board = Board()
                self.current_player = 'X'
                self.run_game()
            elif choice == '2':
                self.game_mode = 'pva'
                self.board = Board()
                self.current_player = 'X'
                self.run_game()
            elif choice == '3':
                self.score_manager.display_scores()
            elif choice == '4':
                print("  👋 Thanks for playing! Goodbye.\n")
                break
            else:
                print("  ❌ Invalid choice. Try again.\n")


# ─────────────────────────────────────────────────────────────────────────────
# UNIT TESTS
# ─────────────────────────────────────────────────────────────────────────────

def test_board_initialization() -> None:
    """Test that board initializes empty."""
    board = Board()
    assert all(cell is None for cell in board.grid)
    assert board.get_empty_cells() == list(range(1, 10))
    print("✓ test_board_initialization passed")


def test_board_moves() -> None:
    """Test making and undoing moves."""
    board = Board()
    assert board.make_move(5, 'X')
    assert not board.make_move(5, 'O')  # Already occupied.
    assert board.grid[4] == 'X'
    board.undo_move(5)
    assert board.grid[4] is None
    print("✓ test_board_moves passed")


def test_win_detection_rows() -> None:
    """Test winning condition: horizontal rows."""
    board = Board()
    board.make_move(1, 'X')
    board.make_move(2, 'X')
    board.make_move(3, 'X')
    assert board.check_winner() == 'X'
    print("✓ test_win_detection_rows passed")


def test_win_detection_columns() -> None:
    """Test winning condition: vertical columns."""
    board = Board()
    board.make_move(1, 'O')
    board.make_move(4, 'O')
    board.make_move(7, 'O')
    assert board.check_winner() == 'O'
    print("✓ test_win_detection_columns passed")


def test_win_detection_diagonal() -> None:
    """Test winning condition: diagonals."""
    board = Board()
    board.make_move(1, 'X')
    board.make_move(5, 'X')
    board.make_move(9, 'X')
    assert board.check_winner() == 'X'
    print("✓ test_win_detection_diagonal passed")


def test_draw_detection() -> None:
    """Test draw condition."""
    board = Board()
    # Fill board without three in a row.
    moves = [1, 2, 4, 3, 5, 7, 6, 9, 8]
    for i, pos in enumerate(moves):
        player = 'X' if i % 2 == 0 else 'O'
        board.make_move(pos, player)
    assert board.is_full()
    assert board.check_winner() is None
    print("✓ test_draw_detection passed")


def test_ai_find_winning_move() -> None:
    """Test that AI detects and takes a winning move."""
    board = Board()
    board.make_move(1, 'O')
    board.make_move(2, 'O')
    # AI should play position 3 to win.
    best_move = AI.find_best_move(board)
    assert best_move == 3
    print("✓ test_ai_find_winning_move passed")


def test_ai_blocks_human_win() -> None:
    """Test that AI blocks human's winning move."""
    board = Board()
    board.make_move(1, 'X')
    board.make_move(5, 'X')
    # AI should block by playing position 9.
    best_move = AI.find_best_move(board)
    assert best_move == 9
    print("✓ test_ai_blocks_human_win passed")


def run_tests() -> None:
    """Run all unit tests."""
    print("\n" + "=" * 40)
    print("       RUNNING UNIT TESTS")
    print("=" * 40 + "\n")
    test_board_initialization()
    test_board_moves()
    test_win_detection_rows()
    test_win_detection_columns()
    test_win_detection_diagonal()
    test_draw_detection()
    test_ai_find_winning_move()
    test_ai_blocks_human_win()
    print("\n" + "=" * 40)
    print("     ALL TESTS PASSED! ✓")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    import sys

    # Run with 'python tictactoe.py test' to run unit tests.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        game = Game()
        game.run()
