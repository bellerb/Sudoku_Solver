import numpy as np
from copy import deepcopy
from random import choices

class Sudoku:
    def __init__(self, size=9, square=3):
        self.size = size
        self.square = square
        self.board = self.generate_board()
        
    def generate_board(self):
        p_nums = [str(i + 1) for i in range(self.size)]
        #Build solvable game board
        while True:
            check = True
            x_hold = [[] for _ in range(self.size)]
            y_hold = [[] for _ in range(self.size)]
            s_hold = [[] for _ in range(self.square ** 2)]
            self.board = [['.' for _ in range(self.size)] for _ in range(self.size)]
            for y in range(self.size):
                for x in range(self.size):
                    m_nums = [n for n in p_nums if n not in s_hold[(x // self.square) + ((y // self.square) * self.square)] and n not in y_hold[y] and n not in x_hold[x]]
                    if len(m_nums) > 0:
                        num = choices(m_nums, k=1)[0]
                        self.board[y][x] = num
                        x_hold[x].append(num)
                        y_hold[y].append(num)
                        s_hold[(x // self.square) + ((y // self.square) * self.square)].append(num)
                    else:
                        check = False
                        break
                if check == False:
                    break
            if check == True:
                break
        return self.board
    
    def mask_board(self):
        p_nums = [i for i in range(self.size)]
        i_choice = [8, 9]
        for y in range(self.size):
            i_amt = choices(i_choice, k=1)[0]
            i_pos = choices(p_nums, k=i_amt)
            self.board[y] = ['.' if i not in i_pos else x for i, x in enumerate(self.board[y])]

game = Sudoku()

solution = game.board
game.mask_board()
m_board = game.board

print(np.array(m_board))

def search_tree(p_moves, board, x_hold, y_hold, s_hold, p_nums, square=3, y=0, x=0):
    if x == 9:
        y += 1
        x = 0
    if (x < len(x_hold) and y < len(y_hold) and x + ((y // square) * square) < len(s_hold)):
        #print(p_moves[y][x])
        if board[y][x] == '.':
            for p in p_moves[y][x]:
                print('---')
                print(x, y, x + ((y // square) * square))
                print(p)
                print(x_hold[x])
                print(y_hold[y])
                print(s_hold[x + ((y // square) * square)])
                print(np.array(board))
                if p not in x_hold[x] and p not in y_hold[y] and p not in s_hold[x + ((y // square) * square)]:
                    print(f'guess')
                    temp_board = deepcopy(board)
                    temp_x_hold = deepcopy(x_hold)
                    temp_y_hold = deepcopy(y_hold)
                    temp_s_hold = deepcopy(s_hold)
                    
                    temp_board[y][x] = p
                    temp_x_hold[x].append(p)
                    temp_y_hold[y].append(p)
                    temp_s_hold[(x // square) + ((y // square) * square)].append(p)
                    
                    temp_board = search_tree(p_moves, temp_board, temp_x_hold, temp_y_hold, temp_s_hold, p_nums=p_nums, square=square, y=y, x=x+1)
                    if temp_board is not None and True not in [True for r in temp_board if '.' in r]:
                        return temp_board
                else:
                    print(f'bad')
        else:
            temp_board = search_tree(p_moves, board, x_hold, y_hold, s_hold, p_nums=p_nums, square=square, y=y, x=x+1)
            if temp_board is not None and True not in [True for r in temp_board if '.' in r]:
                return temp_board
    return None
    

def solve_game(board, square=3):
    p_nums = [str(i + 1) for i in range(9)]
    x_hold = [[] for _ in range(9)]
    y_hold = [[] for _ in range(9)]
    s_hold = [[] for _ in range(square ** 2)]
    
    p_board = []
    for l in range(2):
        for y in range(len(board)):
            if l == 1:
                p_board.append([])
            for x in range(len(board[y])):
                if l == 0:
                    if board[y][x] != '.':
                        x_hold[x].append(board[y][x])
                        y_hold[y].append(board[y][x])
                        s_hold[(x // square) + ((y // square) * square)].append(board[y][x])
                else:
                    if board[y][x] == '.':
                        pos_hold = [n for n in p_nums if n not in s_hold[(x // 3) + ((y // 3) * 3)] and n not in y_hold[y] and n not in x_hold[x]]
                        p_board[-1].append(pos_hold)
                    else:
                        p_board[-1].append([board[y][x]])
    print(p_board)
    board = search_tree(p_board, board, x_hold, y_hold, s_hold, p_nums=p_nums, square=square, y=0, x=0)
    print(np.array(board))
    
solve_game(m_board)
