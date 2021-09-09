from board.Board import Board
import re
from piece.Base import InvalidMoveError
import traceback

b = Board()

while True:
    try:
        print(b)
        move = input('Move: ')
        b.move(move)
    except InvalidMoveError as e:
        print(traceback.format_exc())

        print('Not valid move, try again...')

