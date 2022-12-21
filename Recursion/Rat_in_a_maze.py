def can_move(maze, r, c, move):
    
    moves = {"U":(r-1,c), "D":(r+1,c), "L":(r,c-1), "R":(r,c+1)}

    if r == 0:
        moves.pop("U")
    if r == (len(maze)-1):
        moves.pop("D")
    if c == 0:
        moves.pop("L")
    if c == (len(maze)-1):
        moves.pop("R")
    
    if move not in moves:
        return False
    row = moves[move][0]
    col = moves[move][1]
    if maze[row][col] == 0 or maze[row][col] == "x":
        return False
    return True

def move(maze,r, c, move):
    moves = {"U":(r-1,c), "D":(r+1,c), "L":(r,c-1), "R":(r,c+1)} 
    maze[r][c] = "x"
    
    return moves[move]

def solve(maze, res, n, r=0, c=0, step=''):
    if r==n-1 and c==n-1:
        res.append(step)
        return
    
    for i in "DLRU":
        if can_move(maze, r, c, i):
            row, col = move(maze, r, c, i)
            solve(maze, res, n, row, col, step+i)
            maze[r][c] = 1


maze = [
    [0,1,1,1],
    [1,1,1,0],
    [1,0,1,1],
    [0,0,1,1]
]

"""res = []
solve(maze, res, 4)
print(res)"""
class Solution:
    
    def findPath(self, m, n):
        if m[0][0] == 0:
            return []


        def move(maze, r, c, move):
            pos_moves = {"D":(r+1,c), "U":(r-1,c), "L":(r,c-1), "R":(r,c+1)}
            maze[r][c] = "x"
        
            return pos_moves[move]
    
        def is_valid_move(maze, r, c, move, n):
            pos_moves = {"D":(r+1,c),"U":(r-1,c),"L":(r,c-1),"R":(r,c+1)}
            x=n-1
            if r==0:
                pos_moves.pop("U")
            if r==x:
                pos_moves.pop("D")
                
            if c==0:
                pos_moves.pop("L")
            if c==x:
                pos_moves.pop("R")
                
            if move not in pos_moves:
                return False
                
            row = pos_moves[move][0]
            col = pos_moves[move][1]
            
            if maze[row][col] == "x" or maze[row][col] == 0:
                return False
                
            return True
    
        def solve_maze(maze, res, n, r=0, c=0, st=''):
            if r == n-1 and c == n-1:
                res.append(st)
                return
            
            for i in "DLRU":
                if is_valid_move(maze, r, c, i, n):
                    row, col = move(maze, r, c, i)
                    solve_maze(maze, res, n, row, col, st+i)
                    maze[r][c] = 1
    
        res=[]
       
        solve_maze(m,res, n)
        return res

        

ob = Solution()
print(ob.findPath(maze, len(maze)))
