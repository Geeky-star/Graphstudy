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
