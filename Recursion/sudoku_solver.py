class SolveSudoku:
    
    def __init__(self, sudoku, size=3):
        self.sudoku = sudoku
        self.size = size
        self.solve()

    def solve(self):
        n = self.size ** 2
        for row in range(n):
            for col in range(n):
                # if finds any vacant place
                if self.sudoku[row][col] == ".":
                    for num in range(1, n+1):
                        if self.isValid(row, col, num):
                            self.sudoku[row][col] = num
                            if self.solve() == True:
                                return True
                            else:
                                self.sudoku[row][col] = "."
                    return False

        return True

    def isValid(self, row, col, num):
        if self.chk_row_col(row, col, num) is False:
            return False

        if self.chk_subboard(row, col, num) is False:
            return False
        return True

    def chk_row_col(self, row, col, num):
        for i in range(self.size**2):
            if self.sudoku[row][i] == num:
                return False
            if self.sudoku[i][col] == num:
                return False

        return True

    def chk_subboard(self, row, col, num):
        row = row - (row % self.size)
        col = col - (col % self.size)

        for r in range(row, row + self.size):
            for c in range(col, col + self.size):
                if self.sudoku[r][c] == num:
                    return False

        return True


            





if __name__ == "__main__":    
    sdk = [[5,3,".",6,7,8,9,".",2],
            [6,7,2,1,9,5,3,4,8],
            [".",9,8,".",4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,".",4,8,5,6],
            [9,6,".",5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,"."]]

    SolveSudoku(sdk)

    for i in sdk:
        print(i)