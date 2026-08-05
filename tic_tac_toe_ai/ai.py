"""Minimax-based AI for the Tic-Tac-Toe game."""

from typing import List, Optional

try:
    from .utils import check_winner, get_available_moves, is_draw
except ImportError:  # pragma: no cover - fallback for direct script execution
    from utils import check_winner, get_available_moves, is_draw


class MinimaxAI:
    """An unbeatable Tic-Tac-Toe AI using minimax with alpha-beta pruning."""

    def __init__(self, ai_mark: str = "O") -> None:
        self.ai_mark = ai_mark
        self.human_mark = "X" if ai_mark == "O" else "O"

    def get_best_move(self, board: List[str]) -> Optional[int]:
        """Choose the best available move using the minimax algorithm."""
        best_score = -float("inf")
        best_move: Optional[int] = None

        for move in get_available_moves(board):
            board[move - 1] = self.ai_mark
            score = self._minimax(board, 1, False, alpha=-float("inf"), beta=float("inf"))
            board[move - 1] = " "

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(
        self,
        board: List[str],
        depth: int,
        is_maximizing: bool,
        alpha: float,
        beta: float,
    ) -> int:
        """Evaluate the board recursively and return the best score."""
        winner = check_winner(board)
        if winner == self.ai_mark:
            return 10 - depth
        if winner == self.human_mark:
            return depth - 10
        if is_draw(board):
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for move in get_available_moves(board):
                board[move - 1] = self.ai_mark
                score = self._minimax(board, depth + 1, False, alpha, beta)
                board[move - 1] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score

        best_score = float("inf")
        for move in get_available_moves(board):
            board[move - 1] = self.human_mark
            score = self._minimax(board, depth + 1, True, alpha, beta)
            board[move - 1] = " "
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break

        return best_score
