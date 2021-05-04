from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        self.paths = []
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFS(self,visited,path,src,dest):
        
        visited[src] = True
        
        if src == dest:
            self.paths.append(path)
            print("paths is  - ", self.paths)
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
g.addEdge(2, 3)
g.addEdge(3, 3)


if g.transitiveClousure(0,3)==True:
    
    print("yes, path exists")
    
