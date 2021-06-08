def isSafe(graph,n,src,colors,c):
    for i in range(n):
        if graph[src][i]==1 and colors[i]==c:
            return False
            
    return True
    
def graphColoringUtil(graph,n,m,src,colors):
    
    if src==n:
        return True
        
    for c in range(1,m+1):
        if isSafe(graph,n,src,colors,c):
            colors[src] = c
            if graphColoringUtil(graph,n,m,src+1,colors):
                return True
            
            colors[src] = 0
        
    return False
        
def graphColoring(graph,n,m,src):
    
    colors = [0]*n
    if graphColoringUtil(graph,n,m,0,colors)==False:
        print("Solution does not exists")
        
    print(colors)


graph = [[0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]];
        
m = 3
n= 4
graphColoring(graph,n,m,0)
        
    
    
    
    
