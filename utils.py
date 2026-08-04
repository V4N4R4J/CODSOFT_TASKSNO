"""Utility helpers for the Tic-Tac-Toe game."""

from typing import List, Optional


def display_board(board: List[str]) -> None:
    """Render the board in a clean 3x3 grid."""
    print()
    for row in range(0, 9, 3):
        print(f" {board[row]} | {board[row + 1]} | {board[row + 2]} ")
        if row < 6:
            print("---+---+---")
    print()


def get_available_moves(board: List[str]) -> List[int]:
    """Return a list of empty cell positions as 1-based indices."""
    return [index + 1 for index, cell in enumerate(board) if cell == " "]


def check_winner(board: List[str]) -> Optional[str]:
    """Return the winning mark if one exists, otherwise None."""
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for first, second, third in winning_combinations:
        if board[first] != " " and board[first] == board[second] == board[third]:
            return board[first]

    return None


def is_draw(board: List[str]) -> bool:
    """Return True when the board is full and no winner exists."""
    return not get_available_moves(board) and check_winner(board) is None


def switch_player(current_player: str) -> str:
    """Switch turns between X and O."""
    return "O" if current_player == "X" else "X"
