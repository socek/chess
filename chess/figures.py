class Figure(object):
    def __init__(self, player):
        self.player = player

    def set_board(self, board):
        self.board = board


class Pawn(Figure):
    name = 'pawn'


class Rook(Figure):
    name = 'rook'


class Knight(Figure):
    name = 'knight'


class Bishop(Figure):
    name = 'bishop'


class Queen(Figure):
    name = 'queen'


class King(Figure):
    name = 'king'
