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
        indegree = [0]*self.v 
        q = deque()
        q.append(src)
        visited[src] = True 
    
        while len(q) > 0:
            node = q.pop()
            for nbr in self.graph[node]:
                if visited[nbr] == False:
                    visited[nbr] = True 
                    q.append(nbr)
                indegree[nbr]+=1 
                    
                    
        print("indegree of given vertex is - ",indegree[src])

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(2,3)

g.bfs(1)
