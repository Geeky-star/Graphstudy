n = 8

def isSafe(mat,i,j):
     if i>=0 and j>=0 and i<8 and j<8 and mat[i][j]==-1:
          return True
           
     return False

def printSolution(n,board):
    
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
 
def dfs(n):
    
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board = [[-1 for i in range(n)] for j in range(n)]
    board[0][0] = 0
    
    pos = 1
   
    if(not dfsUtil(8,board,0,0,move_x,move_y,pos)):
        print("Solution does not exist")
    else:
        printSolution(n,board)
    
def dfsUtil(n,board,curx,cury,move_x,move_y,pos):
     
    if(pos == n**2):
        return True
 
    for i in range(8):
        new_x = curx + move_x[i]
        new_y = cury + move_y[i]
        if(isSafe(board,new_x, new_y)):
            board[new_x][new_y] = pos
            if(dfsUtil(n,board,new_x,new_y,move_x,move_y,pos+1)):
                return True
 
            board[new_x][new_y] = -1
    
    return False
    
    
dfs(n)
