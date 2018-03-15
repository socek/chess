from chess.sides import Black
from chess.sides import White


class Board(object):
    def start_game(self):
        self.board = [[None for loop in range(8)] for loop in range(8)]
        self.players = [White(), Black()]

        for player in self.players:
            player.start_game(self)

    def put_figure(self, figure, y, x):
        figure.set_board(self)
        self.board[y][x] = figure

    def get_figure(self, y, x):
        return self.board[y][x]

    def get_figure_position(self, figure):
        for y, line in enumerate(self.board):
            for x, obj in enumerate(line):
                if figure == obj:
                    return y, x

    def move_figure(self, figure, y, x):
        current_y, current_x = self.get_figure_position(figure)

        self.board[current_y][current_x] = None
        self.board[y][x] = figure
