from collections import defaultdict

class Graph:
    
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
        
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
        
    def DFS(self,graph,v,visited,arrival,departure,time):
    
       time += 1
       visited[v] = True
    
       arrival[v] = time
    
       for nbr in self.graph[v]:
          if visited[nbr]==False:
             time = self.DFS(self.graph,nbr,visited,arrival,departure,time)
            
       time += 1
       departure[v] = time
       
       return time
        
g = Graph(8)
n=8

g.addEdge(0,1)
g.addEdge(0,2)

g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,1)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(6,7)

arrival = [None]*n
departure = [None]*n

visited = [False]*n
time = -1

for i in range(n):
    
    if visited[i]==False:
        time = g.DFS(g,i,visited,arrival,departure,time)
        print("time is ",time)
        
for j in range(n):
    print("time of ", j ," ", (arrival[j],departure[j]))
    
