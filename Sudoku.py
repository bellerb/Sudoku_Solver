import numpy as np
from random import shuffle

class Sudoku:
    def __init__(self, size=9, square=3):
        self.size = size
        self.square = square
        self.x_hold = {}
        self.y_hold = {}
        self.s_hold = {}
        self.placed = [(x, y) for y in range(9) for x in range(9)]
        self.p_nums = [str(i + 1) for i in range(self.size)]
        self.board = [[]]
        self.generate_board()
        
    def generate_board(self):
        if len(self.placed) == 0:
            return True
        x, y = self.placed[0]
        s = (x // self.square) + ((y // self.square) * self.square)
        m_nums = [n for n in self.p_nums if (s not in self.s_hold or n not in self.s_hold[s]) and (x not in self.y_hold or n not in self.y_hold[x]) and (y not in self.x_hold or n not in self.x_hold[y])]
        if len(m_nums) > 0:
            shuffle(m_nums)
            for n in m_nums:
                self.placed = self.placed[1:]
                if len(self.board) >= y + 1:
                    if len(self.board[y]) >= x + 1:
                        self.board[y][x] = n
                    else:
                        self.board[y].append(n)
                else:
                    self.board.append([n])
                if x in self.y_hold:
                    self.y_hold[x].append(n)
                else:
                    self.y_hold[x] = [n]
                if y in self.x_hold:
                    self.x_hold[y].append(n)
                else:
                    self.x_hold[y] = [n]
                if s in self.s_hold:
                    self.s_hold[s].append(n)
                else:
                    self.s_hold[s] = [n]
                if self.generate_board():
                    return True
                else:
                    self.placed.insert(0, (x, y))
                    self.y_hold[x] = self.y_hold[x][:-1]
                    self.x_hold[y] = self.x_hold[y][:-1]
                    self.s_hold[s] = self.s_hold[s][:-1]
                    self.board[y][x] = '.'
        return False
    
    def mask_board(self, i_choice = [1, 3]):
        p_nums = [i for i in range(self.size)]
        for y in range(self.size):
            i_amt = choices(i_choice, k=1)[0]
            i_pos = choices(p_nums, k=i_amt)
            self.board[y] = ['.' if i not in i_pos else x for i, x in enumerate(self.board[y])]

game = Sudoku()

solution = game.board
print(np.array(solution))
game.mask_board([5,8])
m_board = game.board
print()
print(np.array(m_board))

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
