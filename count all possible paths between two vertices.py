from collections import defaultdict

class Graph:
     
    def __init__(self,v):
         self.v = v
         self.graph = defaultdict(list)
         self.count=0
        
    def addEdge(self,u,v):
         self.graph[u].append(v)
       
    def dfs(self,src,dest,visited):
        
        visited[src] = True
    
        if src==dest:
           self.count+=1
          
        for nbr in self.graph[src]:
               if visited[nbr]==False:
                    self.dfs(nbr,dest,visited)
                    
                    
        visited[src] = False
        
    def dfsUtil(self,src,dest):
    
         visited = [False]*self.v
         self.dfs(src,dest,visited)
         print("count is -    ",self.count)
         
         
g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(1,3)

s = 2
d = 3

g.dfsUtil(2,3)
