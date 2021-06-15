from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self,v):
        self.v = v 
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def isCyclicUtil(self,src,visited,parent):
        
        visited[src] = True 
        
        for nbr in self.graph[src]:
            if visited[nbr]==False:
                if self.isCyclicUtil(nbr,visited,src)==True:
                    return True 
                    
            elif nbr!=parent:
                return True 
                
        return False 
        
    def isGraphTree(self):
        
        visited = [False]*self.v 
        
        if self.isCyclicUtil(0,visited,-1)==True:
            return False 
            
        for i in range(self.v):
            if visited[i]==False:
                return False
            
        return True 
            
            
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

if g1.isGraphTree()==True:
    print("Yes, Graph is a tree")
else:
    print("No, graph is not a tree")


g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
print("Graph is a Tree" if g2.isGraphTree() == True else "Graph is a not a Tree")
