from piece.Base import Base
from piece.Position import Position



class Bishop(Base):
    PIECE_NAME = "B"
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    @property
    def possible_moves(self):
        col = self.position.col
        row = self.position.row

        moves = []
        # top left
        for x in range(1,7):
            new_r = row + x
            new_c = col - x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if self.board.get_position(row=new_r, col=new_c) != " " :
                break

        # top right
        for x in range(1,7):
            new_r = row + x
            new_c = col + x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if self.board.get_position(row=new_r, col=new_c) != " " :
                break

        # bottom left
        for x in range(1,7):
            new_r = row - x
            new_c = col - x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if self.board.get_position(row=new_r, col=new_c) != " " :
                break

        # bottom right
        for x in range(1,7):
            new_r = row - x
            new_c = col + x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if self.board.get_position(row=new_r, col=new_c) != " " :
                break
        return moves
