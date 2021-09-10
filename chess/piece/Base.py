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
    def possible_moves(self) -> List:
        raise NotImplementedError()

    @property
    def valid_moves(self) -> List:
        valid = []
        for new_position in self.possible_moves:
            new_position_piece = self.board.get_position(position=new_position)
            if isinstance(new_position_piece, Base) and new_position_piece.is_white == self.is_white:
                continue
            valid.append(new_position)
        return valid


    def move(self, target):
        if type(target) == str:
            target = Position(target)
        if target not in self.possible_moves:
            raise InvalidMoveError

        # if new position is in the same team
        new_position_piece = self.board.get_position(position=target)
        if isinstance(new_position_piece, Base) and new_position_piece.is_white == self.is_white:
            raise InvalidMoveError

        self.position = target
        return target

    @property
    def piece_name(self):
        return self.PIECE_NAME.lower() if self.is_white else self.PIECE_NAME.upper()

    def __repr__(self):
        return self.piece_name + self.position.__repr__()

    @property
    def targets(self) -> set:
        return set(self.possible_moves)

