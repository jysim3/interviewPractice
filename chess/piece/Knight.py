from piece.Base import Base
from piece.Position import Position



class Knight(Base):
    PIECE_NAME = "N"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    @property
    def possible_moves(self):
        col = self.position.col
        row = self.position.row

                

        moves = [
            (row+2, col+1),
            (row+2, col-1),
            (row+1, col+2),
            (row+1, col-2),
            (row-1, col+2),
            (row-1, col-2),
            (row-2, col+1),
            (row-2, col-1)
        ]
        moves = [
            Position(row=r, col=c)
            for r,c in moves
            if 0 <= r < 8 and 0 <= c < 8
        ]

        return moves

