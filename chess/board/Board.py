from piece import Bishop, Knight, Pawn, Rook, Queen, King
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
    def __init__(self):
        self.white_turn = True
        self._board = [
                # abcdefgh
            list('rnbqkbnr'), # 1
            list('pppppppp'), # 2
            list('        '), # 3
            list('        '), # 4
            list('        '), # 5 => f5 => board[4][5]
            list('        '), # 6
            list('PPPPPPPP'), # 7
            list('RNBQKBNR'), # 8
        ]
        self._pieces = {}
        for col, line in enumerate(self._board):
            for row, piece_notation in enumerate(line):
                if piece_notation == " ":
                    continue
                position = Position(row=row, col=col)
                piece_class = representation[piece_notation.lower()]
                piece = piece_class(position, piece_notation.islower(), self)

                self._pieces[position.__repr__()] = piece

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
            piece_object = self.get_position(position=origin, pop = True)
            if not piece_object or piece_object.piece_name != piece:
                raise InvalidMoveError("Different/No piece at the selected position, {}<->{}".format(
                    self._board[origin.col][origin.row], piece
                ))
            # try move piece, return new position
            new = piece_object.move(new)
        except InvalidMoveError:
            self._pieces[origin.__repr__()] = piece_object
            raise


        self._pieces[new.__repr__()] = piece_object

        self._board[origin.col][origin.row] = " "
        self._board[new.col][new.row] = piece_object.piece_name

        self.white_turn = not self.white_turn

        white, _ = self.threats

        for piece in self._pieces.values():
            if piece.piece_name == "K" and piece.position in black:
                print("CHECK")
            if piece.piece_name == "k" and piece.position in white:
                print("CHECK")

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

    @property
    def threats(self):
        white = set()
        black = set()
        for piece in self._pieces.values():
            if piece.is_white:
                white = white.union(piece.targets)
            else:
                black = black.union(piece.targets)
        return black, white

