class Figure(object):
    def __init__(self, player):
        self.player = player

    def set_board(self, board):
        self.board = board

    def _can_move(self, moves, y, x):
        if y < 0 or y > 7 or x < 0 or x > 7:
            return False
        if not self.board.get_figure(y, x):
            moves.append((y, x))
            return True
        return False

    def _can_attack(self, moves, y, x):
        if y < 0 or y > 7 or x < 0 or x > 7:
            return False
        figure = self.board.get_figure(y, x)
        if figure and figure.player != self.player:
            moves.append((y, x))
            return True
        return False


class Pawn(Figure):
    name = 'pawn'

    def avalible_moves(self):
        moves = []
        current_y, current_x = self.board.get_figure_position(self)
        possible_y = current_y + self.player.direction
        possible_double_y = current_y + (self.player.direction * 2)

        if self._can_move(moves, possible_y, current_x):
            self._can_move(moves, possible_double_y, current_x)

        self._can_attack(moves, possible_y, current_x - 1)
        self._can_attack(moves, possible_y, current_x + 1)
        self._can_attack(moves, possible_double_y, current_x - 2)
        self._can_attack(moves, possible_double_y, current_x + 2)

        return moves


class Rook(Figure):
    name = 'rook'

    def avalible_moves(self):
        moves = []
        current_y, current_x = self.board.get_figure_position(self)

        for move_y, move_x in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            possible_y = current_y
            possible_x = current_x

            while True:
                possible_y += move_y
                possible_x += move_x

                if not self._can_move(moves, possible_y, possible_x):
                    self._can_attack(moves, possible_y, possible_x)
                    break

        return moves


class Knight(Figure):
    name = 'knight'


class Bishop(Figure):
    name = 'bishop'


class Queen(Figure):
    name = 'queen'


class King(Figure):
    name = 'king'
