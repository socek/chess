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

    def test_avalible_moves_for_pawn(self, board):
        board.start_game()

        pawn = board.get_figure(1, 1)
        assert pawn.avalible_moves() == [
            (2, 1),
            (3, 1),
        ]

    def test_avalible_moves_for_pawn_2(self, board):
        board.start_game()

        black_pawn = board.get_figure(6, 1)
        board.move_figure(black_pawn, 3, 1)

        pawn = board.get_figure(1, 1)
        assert pawn.avalible_moves() == [
            (2, 1),
        ]

    def test_avalible_moves_for_pawn_3(self, board):
        board.start_game()

        black_pawn = board.get_figure(6, 1)
        board.move_figure(black_pawn, 2, 1)

        pawn = board.get_figure(1, 1)
        assert pawn.avalible_moves() == []

    def test_avalible_moves_for_pawn_4(self, board):
        board.start_game()

        black_pawn = board.get_figure(6, 1)
        board.move_figure(black_pawn, 2, 2)

        pawn = board.get_figure(1, 1)
        assert pawn.avalible_moves() == [
            (2, 1),
            (3, 1),
            (2, 2),
        ]

    def test_cannot_move_outside_of_the_board(self, board):
        board.start_game()

        black_pawn = board.get_figure(6, 1)

        assert not black_pawn._can_move([], -1, 0)
        assert not black_pawn._can_move([], 0, -1)
        assert not black_pawn._can_move([], 8, 0)
        assert not black_pawn._can_move([], 0, 8)
        assert not black_pawn._can_attack([], -1, 0)
        assert not black_pawn._can_attack([], 0, -1)
        assert not black_pawn._can_attack([], 8, 0)
        assert not black_pawn._can_attack([], 0, 8)
        assert black_pawn._can_move([], 5, 5)

    def test_rook_move_1(self, board):
        board.start_game()

        rook = board.get_figure(0, 0)

        assert rook.avalible_moves() == []

    def test_rook_move_2(self, board):
        board.start_game()

        pawn = board.get_figure(1, 0)
        rook = board.get_figure(0, 0)

        board.move_figure(pawn, 2, 1)

        assert rook.avalible_moves() == [
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
        ]

    def test_rook_move_3(self, board):
        board.start_game()

        rook = board.get_figure(0, 0)

        board.move_figure(rook, 5, 1)

        assert rook.avalible_moves() == [
            (5, 2),
            (5, 3),
            (5, 4),
            (5, 5),
            (5, 6),
            (5, 7),
            (6, 1),
            (4, 1),
            (3, 1),
            (2, 1),
            (5, 0)
        ]
