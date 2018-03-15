from chess.board import Board
from chess.gui import Gui


def run():
    board = Board()
    board.start_game()

    gui = Gui(board)
    gui.load_images()
    gui.run()


if __name__ == "__main__":
    run()
