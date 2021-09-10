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
        if not isinstance(self.board.get_position(col=col+up,row=row), Base):
            moves.append(Position(col=col+up, row=row))

            # double moves
            if (self.is_white and col == 1) or (not self.is_white and col == 6):
                if not isinstance(self.board.get_position(col=col+up*2,row=row), Base):
                    moves.append(Position(col=col+up*2, row=row))

        # takes
        if row - 1 >= 0:
            top_left = self.board.get_position(col=col+up, row=row-1)
            if top_left and top_left.is_white != self.is_white:
                moves.append(Position(col=col+up, row=row-1))

        if row + 1 < 8:
            top_right = self.board.get_position(col=col+up, row=row+1)
            if top_right and top_right.is_white != self.is_white:
                moves.append(Position(col=col+up, row=row+1))
            

        return moves

    @property
    def targets(self):
        col = self.position.col
        row = self.position.row
        moves = set()
        up = 1 if self.is_white else -1
        # takes
        if row - 1 >= 0:
            moves.add(Position(col=col+up, row=row-1))

        if row + 1 < 8:
            moves.add(Position(col=col+up, row=row+1))
            
        return moves
