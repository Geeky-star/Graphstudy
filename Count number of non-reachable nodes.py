from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self,v):
        self.v = v 
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bfs(self,src):
        
        visited = [False]*self.v 
        q = deque()
        q.append(src)
        visited[src] = True 
        
        while len(q) > 0:
            node = q.pop()
            for nbr in self.graph[node]:
                if visited[nbr] == False:
                    visited[nbr] = True 
                    q.append(nbr)
                    
                    
        count = 0
        for i in range(self.v):
            if visited[i]==False:
                count+=1 
                
        print("Number of non-reachable nodes - ",count)

g = Graph(8)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(6, 7)
                
g.bfs(0)  
