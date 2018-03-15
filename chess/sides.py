from chess.figures import Bishop
from chess.figures import King
from chess.figures import Knight
from chess.figures import Pawn
from chess.figures import Queen
from chess.figures import Rook


class Player(object):
    def start_game(self, board):
        for loop in range(8):
            board.put_figure(Pawn(self), self.pawnline, loop)

        board.put_figure(Rook(self), self.figuresline, 0)
        board.put_figure(Knight(self), self.figuresline, 1)
        board.put_figure(Bishop(self), self.figuresline, 2)
        board.put_figure(Bishop(self), self.figuresline, 5)
        board.put_figure(Knight(self), self.figuresline, 6)
        board.put_figure(Rook(self), self.figuresline, 7)

        board.put_figure(Queen(self), self.figuresline, self.queen_place)
        board.put_figure(King(self), self.figuresline, self.king_place)


class White(Player):
    color = 'white'
    pawnline = 1
    figuresline = 0
    queen_place = 3
    king_place = 4
    direction = 1


class Black(Player):
    color = 'black'
    pawnline = 6
    figuresline = 7
    queen_place = 3
    king_place = 4
    direction = -1
