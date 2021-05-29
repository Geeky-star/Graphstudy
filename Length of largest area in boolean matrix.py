def isSafe(matrix,visited,i,j,row,col):
    
    if i>=0 and j>=0 and i<row and j<col and visited[i][j] == False and matrix[i][j] == 1:
        return True
        
    return False

def dfs(matrix,visited,i,j,row,col,count):
    
    visited[i][j] = True
    
    if isSafe(matrix,visited,i,j,row,col):
        count = count+1
        dfs(matrix,visited,i+1,j,row,col,count)
        dfs(matrix,visited,i-1,j,row,col,count)
        dfs(matrix,visited,i,j+1,row,col,count)
        dfs(matrix,visited,i,j-1,row,col,count)
        dfs(matrix,visited,i-1,j-1,row,col,count)
        dfs(matrix,visited,i+1,j+1,row,col,count)
        dfs(matrix,visited,i+1,j-1,row,col,count)
        dfs(matrix,visited,i-1,j+1,row,col,count)
    
    return count
    
mat = [[0,0,1,1,0],
       [1,0,1,1,0],
       [0,1,0,0,0],
       [0,0,0,0,1]]
       
row = 4
col = 5
visited = [[False for i in range(col)] for j in range(row)]
l = []

for i in range(row):
    for j in range(col):
        if visited[i][j] == False and mat[i][j]==1:
            count = 1
            res = dfs(mat,visited,i,j,row,col,count)
            l.append(res)
        
print(max(l))
