from piece.Base import Base
from piece.Position import Position



class Pawn(Base):
    PIECE_NAME = "P"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    @property
    def possible_moves(self):
        col = self.position.col
        row = self.position.row
        moves = []

        up = 1 if self.is_white else -1

        # moves
        if self.board.get_position(col=col+up, row=row) == ' ':
            moves.append(Position(col=col+up, row=row))

            # double moves
            if (self.is_white and col == 1) or (not self.is_white and col == 6):
                if self.board.get_position(col=col+up*2,row=row) == ' ':
                    moves.append(Position(col=col+up*2, row=row))

        # takes
        if row - 1 >= 0 and self.board.get_position(col=col+up, row=row-1).isupper():
            moves.append(Position(col=col+up, row=row-1))

        if row + 1 < 8 and self.board.get_position(col=col+up, row=row+1).isupper():
            moves.append(Position(col=col+up, row=row+1))
            

        return moves

