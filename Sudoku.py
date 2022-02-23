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
    
    def mask_board(self, i_choice = [1, 3]):
        p_nums = [i for i in range(self.size)]
        for y in range(self.size):
            i_amt = choices(i_choice, k=1)[0]
            i_pos = choices(p_nums, k=i_amt)
            self.board[y] = ['.' if i not in i_pos else x for i, x in enumerate(self.board[y])]

game = Sudoku()

solution = game.board
game.mask_board([1, 4])
m_board = game.board

class SolveSudoku:
    def __init__(self, board, square=3):
        self.square = square #Size of small inner square
        self.x_hold = {} #Row hold
        self.y_hold = {} #Column hold
        self.s_hold = {} #Subgrid hold
        self.empty = [] #Empty square index
        self.p_nums = [str(i + 1) for i in range(len(board))] #Possible numbers
        self.board = board #Game board
        self.solve_game()
        
    def solve_game(self):
        #Find empty squares
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != '.':
                    if y in self.x_hold:
                        self.x_hold[y].append(self.board[y][x])
                    else:
                        self.x_hold[y] = [self.board[y][x]]
                    if x in self.y_hold:
                        self.y_hold[x].append(self.board[y][x])
                    else:
                        self.y_hold[x] = [self.board[y][x]]
                    if (x // self.square) + ((y // self.square) * self.square) in self.s_hold:
                        self.s_hold[(x // self.square) + ((y // self.square) * self.square)].append(self.board[y][x])
                    else:
                        self.s_hold[(x // self.square) + ((y // self.square) * self.square)] = [self.board[y][x]]
                else:
                    self.empty.append((x, y))
        self.search_tree()

    def search_tree(self):
        if len(self.empty) == 0: #If there are no more empty squares
            return True
        x, y = self.empty[0]
        s = (x // self.square) + ((y // self.square) * self.square)
        for p in self.p_nums:
            if (y not in self.x_hold or p not in self.x_hold[y]) and (x not in self.y_hold or p not in self.y_hold[x]) and (s not in self.s_hold or p not in self.s_hold[s]):
                self.board[y][x] = p
                if y in self.x_hold:
                    self.x_hold[y].append(p)
                else:
                    self.x_hold[y] = [p]
                if x in self.y_hold:
                    self.y_hold[x].append(p)
                else:
                    self.y_hold[x] = [p]
                if s in self.s_hold:
                    self.s_hold[s].append(p)
                else:
                    self.s_hold[s] = [p]
                self.empty = self.empty[1:]
                if self.search_tree():
                    return True
                else:
                    #Backtrack to previous node in tree
                    self.board[y][x] = '.'
                    self.x_hold[y] = self.x_hold[y][:-1]
                    self.y_hold[x] = self.y_hold[x][:-1]
                    self.s_hold[s] = self.s_hold[s][:-1]
                    self.empty.insert(0, (x, y))
        return False

print(np.array(m_board))
print()
SolveSudoku(m_board) #Solve game in place
print(np.array(m_board))
