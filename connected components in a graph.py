from collections import defaultdict

class Graph:
     
    def __init__(self,v):
         self.v = v
         self.graph = defaultdict(list)
         self.paths = []
        
    def addEdge(self,u,v):
         self.graph[u].append(v)
       
    def dfs(self,src,visited,path):
    
        visited[src] = True
        for nbr in self.graph[src]:
               if visited[nbr]==False:
                    path.append(nbr)
                    self.dfs(nbr,visited,path)
        
        return path
               
        
    def dfsUtil(self):
    
         visited = [False]*self.v
         
         for i in range(self.v):
              if visited[i]==False:
                  temp = self.dfs(i,visited,[i])
                  if temp!=[]:
                     self.paths.append(temp)
         
         print("connected components are -    ",self.paths)
         print("total number of trees in forest are -    ",len(self.paths))
         

g = Graph(5)
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(2,3)
g.addEdge(3, 4) 

g.dfsUtil()
