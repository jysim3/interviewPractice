from piece import Bishop, Knight, Pawn, Rook, Queen, King
from piece.Position import Position
from piece.Base import InvalidMoveError
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
        self.board = [
                # abcdefgh
            list('rnbqkbnr'), # 1
            list('pppppppp'), # 2
            list('        '), # 3
            list('        '), # 4
            list('     q  '), # 5 => f5 => board[4][5]
            list('        '), # 6
            list('PPPPPPPP'), # 7
            list('RNBQKBNR'), # 1
        ]

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
        if self.board[origin.col][origin.row] != piece:
            raise InvalidMoveError("Different/No piece at the selected position, {}<->{}".format(
                self.board[origin.col][origin.row], piece
            ))
        
        # get piece
        piece_object = representation[piece.lower()](origin, piece.islower(), self)
        # try move piece, return new position
        new = piece_object.move(new)

        self.board[origin.col][origin.row] = " "
        self.board[new.col][new.row] = piece

        self.white_turn = not self.white_turn

    def __repr__(self):
        return '\n'.join(reversed(list(''.join(y for y in x) for x in self.board)))

    def get_position(self, row=None, col=None, position=None):
        if position:
            if type(position) == str:
                position = Position(r=position)
        else:
            position = Position(row=row, col=col)

        return self.board[position.col][position.row]

