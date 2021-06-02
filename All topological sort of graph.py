from collections import defaultdict

class Graph:

    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
        self.indegree = [0]*self.v
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.indegree[v] += 1
        
    def dfsUtil(self,visited,stack):
         
        for src in range(self.v):
         
          if self.indegree[src]==0 and visited[src]==False:
                
                for nbr in self.graph[src]:
                    self.indegree[nbr] -= 1
                
                visited[src] = True
                stack.append(src)
                self.dfsUtil(visited,stack)
          
                for k in self.graph[src]:
          
                     self.indegree[k] += 1
               
                stack.pop()
                visited[src] = False
          
        if len(stack)==self.v:
              print(stack)
    
          
          
          
    
    def dfs(self):
        
        visited = [False]*self.v
        stack = []
        self.dfsUtil(visited,stack)
             
             
             
             
g = Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)
g.dfs()
        
