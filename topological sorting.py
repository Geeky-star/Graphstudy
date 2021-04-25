def topoSort(self, V, adj):
        
        def topoSortUtil(v,visited,stack):
            visited[v] = True
            for i in self.adj[v]:
               if visited[i] == False:
                  topoSortUtil(i,visited,stack)
                
            stack.insert(0,v)
        
        
        visited = [False]*self.V
        stack = []
        
        for i in range(self.V):
            if visited[i] == False:
                topoSortUtil(i,visited,stack)
                
        return stack
