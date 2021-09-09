from piece.Base import Base
from piece.Position import Position



class Rook(Base):
    PIECE_NAME="R"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    @property
    def possible_moves(self):
        col = self.position.col
        row = self.position.row
        moves = []

        # right
        for r in range(1,7):
            new_r = r + row
            if not 0 < new_r < 8:
                break
            moves.append(Position(row=new_r, col=col))
            if self.board.get_position(row=new_r, col=col) != " " :
                break

        # left
        for r in range(-1, -7, -1):
            new_r = r + row
            if not 0 < new_r < 8:
                break
            moves.append(Position(row=new_r, col=col))
            if self.board.get_position(row=new_r, col=col) != " " :
                break

        # up
        for c in range(1,7):
            new_c = c + col
            if not 0 < new_c < 8:
                break
            moves.append(Position(col=new_c, row=row))
            if self.board.get_position(col=new_c, row=row) != " " :
                break

        # down
        for c in range(-1, -7, -1):
            new_c = c + col
            if not 0 < new_c < 8:
                break
            moves.append(Position(col=new_c, row=row))
            if self.board.get_position(col=new_c, row=row) != " " :
                break

        return moves

