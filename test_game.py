"""Simple smoke tests for the Tic-Tac-Toe package."""

from tic_tac_toe_ai.game import TicTacToeGame
from tic_tac_toe_ai.utils import check_winner, is_draw


def test_initial_state() -> None:
    game = TicTacToeGame()
    assert game.board.count(" ") == 9
    assert game.current_player == "X"


def test_winning_line() -> None:
    game = TicTacToeGame()
    game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert check_winner(game.board) == "X"


def test_draw_detection() -> None:
    game = TicTacToeGame()
    game.board = ["X", "O", "X", "X", "X", "O", "O", "X", "O"]
    assert is_draw(game.board) is True
