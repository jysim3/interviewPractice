

class InvalidPositionError(Exception):
    pass




class Position():
    def __init__(self, r: str=None, row: int=None, col: int=None):
        if r:
            self.position = r
        elif row is not None and col is not None:
            if row < 0 or row > 7 or col < 0 or col > 7:
                raise InvalidPositionError("{row}, {col} is not a valid position".format(row=row, col=col))
            self.position = chr(row + 97) + str(col + 1) 
        else:
            raise Exception()

    @property
    def row(self):
        return ord(self.position[0]) - 97

    @property
    def col(self):
        return int(self.position[1]) - 1

    def __repr__(self):
        return self.position
    
    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.__repr__() < other.__repr__()

