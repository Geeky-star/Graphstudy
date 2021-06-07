class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
   
    def pathMoreThanK(self,src, k):
        visited = [False]*self.V
        visited[src] = 1
       
        return self.pathMoreThanKUtil(src, k, visited)
       
    def pathMoreThanKUtil(self,src, k, visited):
        if (k <= 0):
            return True
       
        for i in range(len(self.adj[src])):
            v = self.adj[src][i][0]
            w = self.adj[src][i][1]
       
            if (visited[v] == True):
                continue
       
            if (w >= k):
                return True
                
            visited[v] = True
       
            if (self.pathMoreThanKUtil(v, k-w,visited)):
                return True
       
            visited[v] = False
       
        return False

    def addEdge(self,u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])
   

if __name__ == '__main__':
  
    V = 9
    g = Graph(V)
   
    #  making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
   
    src = 0
    k = 62
    if g.pathMoreThanK(src, k):
        print("Yes")
    else:
        print("No")
   
    k = 60
    if g.pathMoreThanK(src, k):
        print("Yes")
    else:
        print("No")
