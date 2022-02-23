import numpy as np

from Sudoku import Sudoku
from Solver import SolveSudoku

game = Sudoku()

print(np.array(game.board))
game.mask_board([5,8])
print()
print(np.array(game.board))
print()
SolveSudoku(game.board)
print(np.array(game.board))
