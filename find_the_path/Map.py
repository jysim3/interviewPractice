

from random import randint
from math import sqrt




class Map():
    def __init__(self, N=40):
        self.N = N
        self.board = [
            list("_" for _ in range(N)) for _ in range(N)
        ]
        self.insert_obstacle(next(self.generate_obstacles()), (2,4))
        self.insert_obstacle(next(self.generate_obstacles()), (N-15,N-15))
        for i in self.generate_obstacles():
            self.insert_obstacle(i)

        self.start = (2,5)
        self.end = (N-2,N-2)
        self.board[self.start[0]][self.start[1]] = "+"
        self.board[self.end[0]][self.end[1]] = "+"

    def valid(self, x, y):
        return (0 <= x < self.N) and (0 <= y < self.N) and self.board[x][y] != "X"
            

    def generate_obstacles(self, size=10):

        yield [ (x,0) for x in range(size)] + [(0,x) for x in range(size)] + [(size-1,x) for x in range(size)]
        yield [ (0,x) for x in range(size)] + [(size-1,x) for x in range(size)] + [(x,size-1) for x in range(size)]
        yield [ (x,0) for x in range(size)] + [(size-1,x) for x in range(size)] + [(x,size-1) for x in range(size)]
        yield [ (x,0) for x in range(size)] + [(0,x) for x in range(size)] + [(x,size-1) for x in range(size)]



    def get_displacement(self, x1, y1, x2, y2):
        return sqrt((x1 - x2)**2  + (y1 - y2)**2)

    def insert_obstacle(self, obstacle, p=None):
        if not p:
            starting_x = randint(0, self.N-1)
            starting_y = randint(0, self.N-1)
        else:
            starting_x = p[0]
            starting_y = p[1]

        for x, y in obstacle:
            try:
                self.board[x + starting_x][y + starting_y] = "X"
            except IndexError:
                pass

    def draw(self, x, y, symbol='*'):
        self.board[x][y] = symbol

    def __repr__(self):
        return '\n'.join(''.join(x) for x in self.board)

