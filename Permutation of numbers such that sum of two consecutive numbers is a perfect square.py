def isSafe(v,graph,path,pos):
    
    if graph[path[pos-1]][v] == 0:
        return False
        
    for i in range(pos):
         if path[i]==v:
            return False 
            
    return True 
    
def formPath(graph,path,pos):
    
    n = len(graph)-1 
    if pos==n+1:
       return True 
       
    for v in range(1,n+1):
       
       if isSafe(v,graph,path,pos):
          path[pos] = v 
          
          if formPath(graph,path,pos+1):
             return True 
          
          path[pos] = -1 
          
    return False 
    
def hamPath(n):
   
   if n==1:
      return "No Solution"
      
   l = list()
   
   for i in range(1,int((2*n-1)**0.5) + 1):
         l.append(i**2)
         
   graph = [[0 for i in range(n+1)] for j in range(n+1)]
   
   for i in range(1,n+1):
       for ele in l:
           
           if ele-i > 0 and ele-i <= n and 2*i!=ele:
                 graph[i][ele-i] = 1 
                 graph[ele-i][i] = 1 
                 
   for j in range(1,n+1):
      path = [-1 for k in range(n+1)]
      path[1] = j 
      
      if formPath(graph,path,2):
         return path[1:]
         
   return "No solution"
   
print(17, '->', hamPath(17))
print(20, '->', hamPath(20))
print(25, '->', hamPath(25))
    
