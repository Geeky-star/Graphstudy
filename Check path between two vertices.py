#Using dfs

paths = []

from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFS(self,visited,path,src,dest):
        
        visited[src] = True
        
        if src == dest:
            paths.append(path)
            print("paths is  - ", paths)
            print("yes path exists")
            return True;
        
        for nbr in self.graph[src]:
            
            if visited[nbr] == False:
                path.append(nbr)
                self.DFS(visited,path,nbr,dest)
                
        
        
    def transitiveClousure(self,src,dest):
        
        
        visited = [False] * self.v
        if self.DFS(visited,[src],src,dest)==True:
                return True
                    
        return False
        
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2,3)
g.addEdge(3, 3)

g.transitiveClousure(1,3)
    
if paths ==[]:
    print("no, path doesn't exists")
    
else:
    print("yes, path exists" , paths)

    
    
#Method 2 - Using bfs


from collections import defaultdict
from collections import deque

class Graph:
    
    def __init__(self,v):
        self.v = v 
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def bfs(self,src,dest):
        
        q = deque()
        q.append(src)
        visited = [False]*self.v
        while len(q)>0:
                
            node = q.pop()
            visited[node]=True 
            if node==dest:
                return True
                
            for nbr in self.graph[node]:
                if visited[nbr]==False:
                    q.append(nbr)
                    
            
        return False
        
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
u = 1 
v = 3 
if g.bfs(1,3)==True:
    print("path found")
else:
    print("no path found")
    
