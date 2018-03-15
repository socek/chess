from pytest import fixture
from pytest import mark

from chess.board import Board


class TestBoard(object):
    @fixture
    def board(self):
        return Board()

    @mark.parametrize('player_index', [0, 1])
    def test_pawns_at_start(self, board, player_index):
        board.start_game()
        player = board.players[player_index]

        for index in range(8):
            figure = board.get_figure(player.pawnline, index)
            figure.name == 'pawn'
            assert figure.player == player

    @mark.parametrize('player_index, places,figure_name', [
        (0, (0, 7), 'rook'),
        (0, (1, 6), 'knight'),
        (0, (2, 5), 'bishop'),
        (1, (0, 7), 'rook'),
        (1, (1, 6), 'knight'),
        (1, (2, 5), 'bishop'),
    ])
    def test_figures_at_start_for_white(self, board, player_index, places,
                                        figure_name):
        board.start_game()
        player = board.players[player_index]

        for index in places:
            figure = board.get_figure(player.figuresline, index)
            figure.name == figure_name
            assert figure.player == player
