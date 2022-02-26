from math import ceil
from random import shuffle, choices

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
    
    def mask_board(self, i_choice = [2, 3], hints=17):
        h_count = 0
        p_nums = [i for i in range(self.size)]
        for y in range(len(self.board)):
            i_amt = choices(i_choice, k=1)[0]
            if h_count + i_amt > hints:
                i_amt = hints - h_count
            elif i_amt < (hints - h_count) // (9 - y):
                i_amt = ceil((hints - h_count) / (9 - y))
            shuffle(p_nums)
            i_pos = p_nums[:i_amt]
            self.board[y] = ['.' if i not in i_pos else x for i, x in enumerate(self.board[y])]
            h_count += i_amt
