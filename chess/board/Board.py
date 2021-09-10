from piece import Bishop, Knight, Pawn, Rook, Queen, King
from copy import deepcopy
from piece.Position import Position
from piece.Base import InvalidMoveError, Base as BasePiece
from typing import Union
import re


representation = {
    "r":   Rook,
    "n":   Knight,
    "b":   Bishop,
    "q":   Queen,
    "k":   King,
    "p":   Pawn,
}

class Board():
    def __init__(self, board = None, dry_run = False, white_turn=True):
        self.dry_run = dry_run
        self.black_checked = False
        self.white_checked = False
        self.white_turn = white_turn
        if not board:

            self._board = list(reversed([
                    # abcdefgh
                list('RNB KBNR'), # 1
                list('PPPPP  P'), # 2
                list('        '), # 3
                list('       Q'), # 4
                list('q       '), # 5 => f5 => board[4][5]
                list('        '), # 6
                list('pppppppp'), # 7
                list('rnbkqbnr'), # 8
            ]))
        else:
            self._board = deepcopy(board)
        self._pieces = {}
        for col, line in enumerate(self._board):
            for row, piece_notation in enumerate(line):
                if piece_notation == " ":
                    continue
                position = Position(row=row, col=col)
                piece_class = representation[piece_notation.lower()]
                piece = piece_class(position, piece_notation.islower(), self)

                self._pieces[position.__repr__()] = piece

    def _move_dry_run(self, move):
        test_board = Board(self._board, dry_run = True, white_turn = self.white_turn)
        test_board.move(move)
        return test_board

    def move(self, move):
        match = re.match('([rnbkqpRNBKQP]?)([a-h][1-8])([a-h][1-8])', move)
        if not match:
            raise InvalidMoveError("Please use long notation")

        piece, origin, new = match.groups()

        # assume pawn
        if not piece:
            piece = 'p' if self.white_turn else 'P'

        if self.white_turn != piece.islower():
            raise InvalidMoveError("Wrong turn")

        origin = Position(r=origin)
        # get piece

        try:
            if not self.dry_run:
                test = self._move_dry_run(move)
                if not self.white_turn and test.black_checked:
                    raise InvalidMoveError("Move places King in checked")
                if self.white_turn and test.white_checked:
                    raise InvalidMoveError("Move places King in checked")

        except InvalidMoveError:
            raise
        piece_object = self.get_position(position=origin, pop = True)
        if not piece_object or piece_object.piece_name != piece:
            raise InvalidMoveError("Different/No piece at the selected position, {}<->{}".format(
                self._board[origin.col][origin.row], piece
            ))
        # try move piece, return new position
        new = piece_object.move(new)


        self._pieces[new.__repr__()] = piece_object

        self._board[origin.col][origin.row] = " "
        self._board[new.col][new.row] = piece_object.piece_name

        self.white_turn = not self.white_turn

        white_targets, black_targets = self.targets

        self.white_checked = False
        self.black_checked = False
        for piece in self._pieces.values():
            if piece.piece_name == "K" and piece.position in white_targets: # black is checked
                self.black_checked = True
                if not self.dry_run and self.get_checkmate(is_white = False):
                    return True

            if piece.piece_name == "k" and piece.position in black_targets: # white is checked
                self.white_checked = True
                if not self.dry_run and self.get_checkmate(is_white = True):
                    print("CHECKMATED")
                    return True

    def __repr__(self):
        return '\n'.join(reversed(list(''.join(y for y in x) for x in self._board)))

    def get_position(self, row=None, col=None, position=None, pop = False) -> Union[None, BasePiece]:
        if position:
            if type(position) == str:
                position = Position(r=position)
        else:
            position = Position(row=row, col=col)

        if pop:
            return self._pieces.pop(position.__repr__(), None)
        return self._pieces.get(position.__repr__(), None)

    def get_checkmate(self, is_white):
        if self.dry_run:
            return False
        if is_white:
            white_moves, _ = self.possible_moves
            for move in white_moves:
                board = self._move_dry_run(move)
                if not board.white_checked:
                    return False

        return True

    @property
    def possible_moves(self):
        white = set()
        black = set()
        for piece in self._pieces.values():
            if piece.is_white:
                white = white.union(set(piece.piece_name + str(piece.position) + str(x) for x in piece.valid_moves))
            else:
                black = black.union(set(piece.piece_name + str(piece.position) + str(x) for x in piece.valid_moves))
        return white, black

    @property
    def targets(self):
        white = set()
        black = set()
        for piece in self._pieces.values():
            if piece.is_white:
                white = white.union(piece.targets)
            else:
                black = black.union(piece.targets)
        return white, black

