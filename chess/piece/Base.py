from typing import List, Union
from piece.Position import Position
from board import Board

class InvalidMoveError(Exception):
    pass

class Base():

    def __init__(self, position: Union[Position, str], is_white: bool, board: Board):
        if type(position) == str:
            position = Position(r=position)
        self.board = board
        self.is_white = is_white
        self.position = position


    @property
    def possible_moves() -> List:
        raise NotImplementedError()

    def move(self, target):
        if type(target) == str:
            target = Position(target)
        print(self.possible_moves)
        if target not in self.possible_moves:
            raise InvalidMoveError

        # if new position is in the same team
        new_position_piece = self.board.get_position(position=target)
        if new_position_piece != ' ' and new_position_piece.isupper() != self.is_white:
            raise InvalidMoveError

        self.position = target
        return target

    def __repr__(self):
        return self.PIECE_NAME + self.position.__repr__()
