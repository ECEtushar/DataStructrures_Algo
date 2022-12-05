"""
Leetcode's Hard level recursion problem
"""



def place(board, c, r):
    if board[c][r] == "x":
        print("Can't place queen")
        return False

    n = len(board)
    
    for i in range(c+1,n):
        board[i][r] = "x"
    
    row = r
    for i in range(c,n):
        if row == n:
            break
        board[i][row] = "x"
        row+=1
        
    row = r
    for i in range(c,n):
        if row == -1:
            break
        board[i][row] = "x"
        row-=1

    
    board[c][r] = "Q"
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[j][i], end='   ')

        print("\n")
    print("--------------")


def remove(board, c, r):
    n = len(board)

    for i in range(c+1,n):
        board[i][r] = 0
    
    row = r
    for i in range(c,n):
        if row == n:
            break
        board[i][row] = 0
        row+=1
        
    row = r
    for i in range(c,n):
        if row == -1:
            break
        board[i][row] = 0
        row-=1

    print("----Removing----")
    board[c][r] = 0
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[j][i], end='   ')

        print("\n")
    print("--------------")



class NQueen:
    def __init__(self,n):
        self.board = [["." for i in range(n)] for i in range(n)]
        self.res=[]
        self.rec_func(self.board, n, self.res)
        self.print_queens(self.res)


    def rec_func(self,board, n, res, col=0):
        if col==n:
            x = [i.copy() for i in board]
            res.append(x)
            return
        for i in range(n):
            if self.is_valid(board, col, row = i):
                board[col][i] = "Q"
                self.rec_func(board, n, res, col+1)
                board[col][i] = "."

    def is_valid(self,board, col, row ):
            if self.l_diagonal_traversal(board, col, row) and self.u_diagonal_traversal(board, col, row) and self.horizontal_traversal(board, col, row):
                return True
            else:
                return False

    def horizontal_traversal(self,board, col, row):
        for i in range(col-1,-1,-1):
            if board[i][row] == "Q":
                return False

        return True


    def u_diagonal_traversal(self,board, col, row):
        col=col-1
        for i in range(row-1,-1,-1):
            if col == -1:
                return True
            if board[col][i] == "Q":
                return False
            col-=1
        return True


    def l_diagonal_traversal(self,board, col, row):
        n = len(board)
        col=col-1
        for i in range(row+1,n):
            if col == -1:
                return True
            if board[col][i] == "Q":
                return False
            col-=1
        return True


    def print_queens(self,queens):
        n=len(queens[0])
        for board in queens:
            for i in range(len(board)):
                for j in range(len(board)):
                    print(board[j][i], end='    ')

                print("\n")
            print(n*"----")

    


NQueen(4)