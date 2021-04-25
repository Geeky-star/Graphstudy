def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        
        def dfs(graph,src,path,visited):
            visited.add(src)
            if src==len(graph)-1:
                paths.append(path)
                return
            
            
            for nbr in graph[src]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(graph,nbr,path + [nbr],visited)
                    visited.remove(nbr)
                
        
        visited = set()
        dfs(graph,0,[0],visited)
        
                
        return paths
            
        
       
           
