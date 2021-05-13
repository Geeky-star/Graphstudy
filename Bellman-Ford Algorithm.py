class Graph:
    
    def __init__(self,v):
        self.v = v
        self.graph = []
        
    def addEdge(self,u,v,w):
        
        self.graph.append([u, v, w])
        
    def printGraph(self,dist):
        
        for i in range(self.v):
            print("{0}\t\t{1}".format(i,dist[i]))
    
    def BellmanFord(self,src):
        
        dist = [float("Inf")] * self.v
        
        dist[src] = 0
        
        for i in range(self.v - 1):
            
            for u,v,w in self.graph:
                
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
                    
            for u,v,w in self.graph:
                
                if dist[u] != float("Inf") and dist[u] + w<dist[v]:
                    
                    print("graph contains a negative cycle")
                    return 
        
        self.printGraph(dist)
        
                
g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
  
g.BellmanFord(0) 

