from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,src):
        
        visited = [False]*self.v
        
        queue = [src]
        visited[src] = True
        while len(queue)>0:
            
            rem = queue.pop(0)
            print(rem,end = " ")
            
            for nbr in self.graph[rem]:
               if visited[nbr]==False:
                  queue.append(nbr)
                  visited[nbr] = True
            
            
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)
