"""Entry point for the terminal-based Tic-Tac-Toe AI game."""

try:
    from .game import TicTacToeGame
except ImportError:  # pragma: no cover - fallback for direct script execution
    from game import TicTacToeGame


def main() -> None:
    """Run the game loop and ask whether the user wants to play again."""
    print("Welcome to Tic-Tac-Toe AI!")
    print("You are X and the AI is O.")
    print("Choose a cell from 1 to 9.")

    while True:
        game = TicTacToeGame()
        game.play_round()

        response = input("Play again? (y/n): ").strip().lower()
        if response not in {"y", "yes"}:
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
