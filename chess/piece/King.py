from piece.Base import Base
from piece.Position import Position



class King(Base):
    PIECE_NAME = "K"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    @property
    def possible_moves(self):
        col = self.position.col
        row = self.position.row
        moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if 0 < row + x < 8 and 0 < col + y < 8:
                    moves.append(Position(row=row+x, col=col+y))

        return moves


