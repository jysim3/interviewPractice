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

        moves = []


        # right
        for r in range(1,7):
            new_r = r + row
            if not 0 < new_r < 8:
                break
            moves.append(Position(row=new_r, col=col))
            if isinstance(self.board.get_position(row=new_r, col=col), Base):
                break

        # left
        for r in range(-1, -7, -1):
            new_r = r + row
            if not 0 < new_r < 8:
                break
            moves.append(Position(row=new_r, col=col))
            if isinstance(self.board.get_position(row=new_r, col=col), Base):
                break

        # up
        for c in range(1,7):
            new_c = c + col
            if not 0 < new_c < 8:
                break
            moves.append(Position(col=new_c, row=row))
            if isinstance(self.board.get_position(col=new_c, row=row), Base):
                break

        # down
        for c in range(-1, -7, -1):
            new_c = c + col
            if not 0 < new_c < 8:
                break
            moves.append(Position(col=new_c, row=row))
            if isinstance(self.board.get_position(col=new_c, row=row), Base):
                break

        # top left
        for x in range(1,7):
            new_r = row + x
            new_c = col - x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if isinstance(self.board.get_position(row=new_r, col=new_c), Base):
                break

        # top right
        for x in range(1,7):
            new_r = row + x
            new_c = col + x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if isinstance(self.board.get_position(row=new_r, col=new_c), Base):
                break

        # bottom left
        for x in range(1,7):
            new_r = row - x
            new_c = col - x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if isinstance(self.board.get_position(row=new_r, col=new_c), Base):
                break

        # bottom right
        for x in range(1,7):
            new_r = row - x
            new_c = col + x
            if not (0 <= new_r < 8 and 0 <= new_c < 8):
                break
            moves.append(Position(row=new_r, col=new_c))
            if isinstance(self.board.get_position(row=new_r, col=new_c), Base):
                break

        return moves
