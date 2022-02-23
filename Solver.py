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
