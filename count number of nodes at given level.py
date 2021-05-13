from collections import deque, defaultdict

class Graph:

    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def bfs(self,s,l):
        
        visited = [False] * self.v
        level = [0]*self.v
        
        queue = deque()
        
        visited[s] = True
        level[s] = 0
        queue.append(s)
        
        while(len(queue)>0):
            
            s = queue.popleft()
            
            for i in self.graph[s]:
                
                if visited[i]==False:
                    level[i] = level[s]+1
                    queue.append(i)
                    visited[i] = True
                    
                    
        count = 0
        for j in range(self.v):
            
            if level[j]==l:
                count+=1
                
        print(count)
        
        
g = Graph(6)      
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
  
level = 2
g.bfs(0, level)
                
