from collections import defaultdict

class Graph:

    def __init__(self,v):
        self.v = v 
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v) 
        self.graph[v].append(u)
        
    def dfsUtil(self,src,visited,path):
         
        visited[src]=True 
        
        for nbr in self.graph[src]:
            if visited[nbr]==False:
                path.append(nbr)
                self.dfsUtil(nbr,visited,path)
         
        return path 
        
    def dfs(self,arr,n):
        
        visited = [False]*(self.v+1) 
        
        for i in arr:
            path = []
            path.append(i)
            if visited[i]==False:
            
                path = self.dfsUtil(i,visited,path)
                visited = [False]*(self.v+1)
                if path!=[]:
                  print("nodes visited from ",i,"are - ",path)
                  
g = Graph(7)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 1)
g.addEdge(5, 6)
g.addEdge(5, 7)

arr = [2,4,5]
n = len(arr)

g.dfs(arr,n)
 
arr = [1,2,5]
n = len(arr)
g.dfs(arr,n)
    
