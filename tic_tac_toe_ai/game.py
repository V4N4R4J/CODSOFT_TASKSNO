"""Game loop and state management for Tic-Tac-Toe."""

from typing import List, Optional

try:
    from .ai import MinimaxAI
    from .utils import check_winner, display_board, is_draw, switch_player
except ImportError:  # pragma: no cover - fallback for direct script execution
    from ai import MinimaxAI
    from utils import check_winner, display_board, is_draw, switch_player


class TicTacToeGame:
    """A terminal-based Tic-Tac-Toe game with an unbeatable AI opponent."""

    def __init__(self) -> None:
        self.board: List[str] = [" "] * 9
        self.current_player = "X"
        self.ai = MinimaxAI(ai_mark="O")

    def reset(self) -> None:
        """Reset the board and player turn for a new game."""
        self.board = [" "] * 9
        self.current_player = "X"

    def make_move(self, position: int, player: str) -> None:
        """Place a mark at the requested cell if it is empty."""
        if not 1 <= position <= 9:
            raise ValueError("Position must be between 1 and 9.")
        if self.board[position - 1] != " ":
            raise ValueError("That cell is already occupied.")
        self.board[position - 1] = player

    def human_move(self) -> None:
        """Prompt the human for a valid move and apply it to the board."""
        while True:
            try:
                choice = input("Choose a position from 1 to 9: ").strip()
                if not choice.isdigit():
                    raise ValueError("Input must be numeric.")

                position = int(choice)
                if not 1 <= position <= 9:
                    raise ValueError("Position must be between 1 and 9.")
                if self.board[position - 1] != " ":
                    raise ValueError("That cell is already occupied.")

                self.make_move(position, "X")
                break
            except ValueError as exc:
                print(f"Invalid move: {exc}")
                print("Please try again.")

    def ai_move(self) -> None:
        """Let the AI choose and play the best move."""
        best_move = self.ai.get_best_move(self.board)
        if best_move is None:
            raise RuntimeError("No valid moves available.")

        self.make_move(best_move, "O")
        print(f"AI plays at position {best_move}.")

    def play_round(self) -> Optional[str]:
        """Run a single round of the game until there is a winner or a draw."""
        self.reset()
        display_board(self.board)

        while True:
            if self.current_player == "X":
                self.human_move()
            else:
                self.ai_move()

            display_board(self.board)

            winner = check_winner(self.board)
            if winner == "X":
                print("Human wins! Good game.")
                return "X"
            if winner == "O":
                print("AI wins! The computer is unbeatable.")
                return "O"
            if is_draw(self.board):
                print("It's a draw!")
                return None

            self.current_player = switch_player(self.current_player)
