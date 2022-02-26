import numpy as np

from Sudoku import Sudoku
from Solver import SolveSudoku

print(
'''
------------------------------
 WELCOME TO THE SUDOKU SOLVER
------------------------------
'''
)
while True:
  print(
'''
\n
----------------------------
 WHAT WOULD YOU LIKE TO DO?
----------------------------
  * Generate Puzzle [G]
  * Solve Puzzle    [P]
\n
'''
  )
  u_in = input()
  if str(u_in).lower() == 'g' str(u_in).lower() == 'generate puzzle':
    option = 0
  elif str(u_in).lower() == 'p' str(u_in).lower() == 'solve puzzle':
    option = 1
    
game = Sudoku()
if option == 0:
  game.mask_board(i_choice=[2,3,4], hints=45)
  print(np.array(game.board))
elif option == 1:
  for y in range(9):
    for x in range(9):
      game.board[y][x] = input(f'x = {x}\ny = {y}\nPlease input the square. ("." = blank & 1-9)\n')
  SolveSudoku(game.board)
  print(np.array(game.board))
