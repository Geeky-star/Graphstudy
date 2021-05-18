def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid)==0 or grid==None:
            return 0
        
        def dfs(grid,row,col,i,j):
                
            if i<0 or j < 0 or i>row-1 or j>col-1 or grid[i][j]=="0":
                return 
            
            else:
                grid[i][j] = "0"
                dfs(grid,row,col,i,j-1)
                dfs(grid,row,col,i-1,j)
                dfs(grid,row,col,i,j+1)
                dfs(grid,row,col,i+1,j)
            
            
        rows = len(grid)
        columns = len(grid[0])
        islands=0
            
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1":
                    grid[i][j]=0
                    islands+=1
                    dfs(grid,rows,columns,i,j)
                    
                    
        return islands
    
