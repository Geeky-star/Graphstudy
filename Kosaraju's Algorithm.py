from collections import defaultdict

class Graph:
    
    def __init__(self,v):
        self.v = v 
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def dfsUtil(self,v,visited):
        
        visited[v] = True 
        print(v,end=" ")
        for nbr in self.graph[v]:
            if visited[nbr]==False:
                self.dfsUtil(nbr,visited)
                
        
    def fillOrder(self,v,visited,stack):
        visited[v] = True 
        
        for nbr in self.graph[v]:
            if visited[nbr]==False:
                self.fillOrder(nbr,visited,stack)
                
        stack.append(v)
                
    def getTranspose(self):
        g = Graph(self.v)
        
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
                
        return g 
        
    def printSCCs(self):
        
        stack = []
        visited = [False]*self.v 
        
        for i in range(self.v):
            if visited[i]==False:
                self.fillOrder(i,visited,stack)
                
        gr = self.getTranspose()
        
        visited = [False]*self.v 
        
        while stack:
            node = stack.pop()
            if visited[node]==False:
                gr.dfsUtil(node,visited)
                print(" ")
                
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
  
   
print("Following are strongly connected components " +
                           "in given graph")
g.printSCCs()

