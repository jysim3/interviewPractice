from piece.Base import Base
from piece.Position import Position



class Queen(Base):
    PIECE_NAME = "Q"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    @property
    def possible_moves(self):
        col = self.position.col
        row = self.position.row

        nyx = [Position(col=col+x, row=row+x) for x in range(-8, 8) if 0 < col + x < 8 and 0 < row + x < 8]
        yx = [Position(col=col-x, row=row+x) for x in range(-8, 8) if 0 < col - x < 8 and 0 < row + x < 8]
        horizontal_moves = [Position(col=x, row=row) for x in range(8) if x != col]
        vertical_moves = [Position(col=col, row=x) for x in range(8) if x != row]

        return sorted([x for x in yx + nyx if x != self.position])

