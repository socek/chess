from chess.sides import Black
from chess.sides import White


class Board(object):
    def start_game(self):
        self.board = [[None for loop in range(8)] for loop in range(8)]
        self.players = [White(), Black()]

        for player in self.players:
            player.start_game(self)

    def put_figure(self, figure, y, x):
        self.board[y][x] = figure
