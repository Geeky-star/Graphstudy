class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 
        self.V = vertices 
  
    def isSafe(self, v,path): 
        if self.graph[path[-1]][v] == 0 or v in path: 
            return False
  
        return True
  
    def hamCycleUtil(self, path): 
  
        if len(path) == self.V: 
            if self.graph[path[-1]][path[0]] == 1: 
                return True
            else: 
                return False
        for v in range(1,self.V): 
  
            if self.isSafe(v,path) == True: 
  
                path.append(v)
  
                if self.hamCycleUtil(path) == True: 
                    return True
  
                path.pop()
  
        return False
  
    def hamCycle(self): 
        path = [] 
        path.append(0)
  
        if self.hamCycleUtil(path) == False: 
            print ("Solution does not exist\n")
            return False
  
        path.append(path[0])
        print(path)
        
        return True
  
g1 = Graph(5) 
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1], 
            [0, 1, 1, 1, 0], ] 
  

g1.hamCycle(); 
  
g2 = Graph(5) 
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0], 
        [0, 1, 1, 0, 0], ] 
  

g2.hamCycle(); 
